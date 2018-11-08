# Title: CafeTask
# Created by: Samit Shaikh
# Created: N/A
# Date of Last Revision: 2018-11-08
# Purpose: To make a working interface for a cafe manager.

import datetime
from _19_InterpreterForCSV import *

nme = os.path.realpath(__file__)


def time(tm):
    tim = str(tm).split(' ')
    halfone = tim[0].split('-')
    halftwo = tim[1].split(':')
    return [int(halfone[2]), int(halfone[1]), int(halfone[0]), int(halftwo[0]), int(halftwo[1]), float(halftwo[2])]


def crct(file):
    if exist(file):
        data = read_csv(file, True)
        try:
            strt = data[0].startswith('!ERROR')
        except AttributeError:
            strt = False
        if strt or not ', '.join(
                data[
                    0]) == 'GNAME, SNAME, ROLE, TRATE, SUPER, HLTH, MON, TUE, WED, THU, FRI, SAT, SUN, LASTCHECKIN, ' \
                           'LASTCHECKOUT, KEY':
            return False
        return True
    else:
        return False


def create(gn, sn, storage):
    def nv(string):
        return str(input(string))

    if not crct(storage):
        print('CREATING NEW DATA CSV')
        write_csv_record(storage, [
            ['GNAME', 'SNAME', 'ROLE', 'TRATE', 'SUPER', 'HLTH', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN',
             'LASTCHECKIN', 'LASTCHECKOUT', 'KEY']])
    print('\nPlease enter the information for ' + gn + ' ' + sn + '.')
    role = nv('ROLE (Barista/Manager): ').strip()
    role = role.lower()
    if role == 'barista' or role == 'manager':
        pass
    else:
        return error(nme, '01_BADINPUT', 'Incorrect ROLE input.')
    trate = nv('TRATE (30/40)').strip()
    if trate == '30' or trate == '40':
        pass
    else:
        return error(nme, '02_BADINPUT', 'Incorrect TRATE input.')
    superr = nv('SUPER (4/6/8)').strip()
    if superr == '4' or superr == '6' or superr == '8':
        pass
    else:
        return error(nme, '03_badinput', 'Incorrect SUPER input.')
    hlth = nv('HLTH (15/25/45)').strip()
    if hlth == '15' or hlth == '25' or hlth == '45':
        pass
    else:
        return error(nme, '04_badinput', 'Incorrect HLTH input.')
    data = read_csv(storage, True)
    key = str(len(data))
    append_csv_record(storage,
                      [gn, sn, role, trate, superr, hlth, 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a',
                       'n/a', key])
    print('CREATED NEW USER DATA')


def checkin(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if (test1 == test2) and (test1 is not None) and (test2 is not None):
        sett = find_csv_record(storage, gn, key='GNAME')
        now = str(datetime.datetime.now())
        update_csv_record(storage, True, int(sett['KEY']), 'LASTCHECKIN', now)
        print('CHECKED IN AT ' + now)
    else:
        return error(nme, '05_NAMENOTFOUND', 'Could not find given name OR username.')


def checkout(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if test1 == test2 and test1 is not None and test2 is not None:
        sett = find_csv_record(storage, gn, key='GNAME')
        now = str(datetime.datetime.now())
        update_csv_record(storage, True, int(sett['KEY']), 'LASTCHECKOUT', now)
        log('THIS DEBUG PAUSE TIME ALLOWS YOU TO CHANGE CSV DATA', logr, wait=True)
        sett = find_csv_record(storage, gn, key='GNAME')
        if time(sett['LASTCHECKOUT'])[2] == time(sett['LASTCHECKIN'])[2]:
            weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
            timee = time(sett['LASTCHECKOUT'])[3] - time(sett['LASTCHECKIN'])[3]
            day = int(datetime.datetime.today().weekday())
            if timee < 0:
                return error(nme, '06_2muchwork', 'Y' + 'OU CANNOT WORK PAST A DAY.'.lower())
            for m in range(7 - day):
                update_csv_record(storage, True, int(sett['KEY']), weekday[day + m], 'n/a')
            update_csv_record(storage, True, int(sett['KEY']), weekday[day], str(timee))
        print('CHECKED OUT AT ' + now)
    else:
        return error(nme, '07_namenotfound', 'Could not find given name and username.')


def wages(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if test1 == test2 and test1 is not None and test2 is not None:
        sett = find_csv_record(storage, gn, key='GNAME')
        weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        wage = 0
        if sett['ROLE'].lower() == 'barista':
            rate = 23
        elif sett['ROLE'].lower() == 'manager':
            rate = 30
        else:
            return error(nme, '08_badrole', 'Incorrectly filled role data.')
        log('role: ' + str(sett['ROLE']), logr)
        for i in range(len(weekday)):
            if not sett[weekday[i]] == 'n/a':
                log(i, logr)
                try:
                    if 0 < int(sett[weekday[i]]) - 9 <= 3 and i <= 4:
                        wagetmp = (9 * rate) + (((int(sett[weekday[i]]) - 9) * rate) * (125 / 100))
                    elif int(sett[weekday[i]]) - 9 > 3 and i <= 4:
                        wagetmp = (9 * rate) + (((int(sett[weekday[i]]) - 9) * rate) * (145 / 100))
                    elif i == 5 and int(sett[weekday[i]]) <= 9:
                        wagetmp = int(sett[weekday[i]]) * (rate + 3)
                    elif i == 6 and int(sett[weekday[i]]) <= 9:
                        wagetmp = int(sett[weekday[i]]) * (rate + 4)
                    elif int(sett[weekday[i]]) - 9 > 0 and i == 5:
                        wagetmp = (9 * (rate + 3)) + (((int(sett[weekday[i]]) - 9) * rate) * (150 / 100))
                    elif int(sett[weekday[i]]) - 9 > 0 and i == 6:
                        wagetmp = (9 * (rate + 4)) + (((int(sett[weekday[i]]) - 9) * rate) * (150 / 100))
                    elif int(sett[weekday[i]]) <= 9 and i <= 4:
                        wagetmp = int(sett[weekday[i]]) * rate
                    else:
                        return error(nme, '09_payrateprob', 'Problem with validating pay rates.')
                    log('wagetmp: ' + str(wagetmp), logr)
                except ValueError:
                    return error(nme, '10_badhourdata', 'Incorrectly filled hour data.')
            else:
                return error(nme, '11_undefinedhours', 'All working hours not defined.')
            wage = wage + wagetmp
        superr = int(sett['SUPER'])
        log('super: ' + str(superr), logr)
        hlth = int(sett['HLTH'])
        log('hlth: ' + str(hlth), logr)
        tax = int(sett['TRATE'])
        log('tax: ' + str(tax), logr)
        log('wage: ' + str(wage), logr)
        log('final: ' + str(((wage * (100 - superr) / 100) - hlth) * (100 - tax) / 100), logr)
        return ((wage * (100 - superr) / 100) - hlth) * (100 - tax) / 100
    else:
        return error(nme, '12_namenotfound', 'Could not find given name and username.')


def run():
    storage = input('CSV Data: ')
    good = crct(storage)
    while True:
        print('!NOTE! This program stores information in ' + storage + '.\nWelcome to Cafe')
        print('Please choose your action: ')
        print('     1 - Check In')
        print('     2 - Check Out')
        print('     3 - Calculate Wages')
        print('     4 - Create Employee Data')
        try:
            x = int(input('  -> '))
        except ValueError:
            return error(nme, '13_badinput', 'Incorrect Input')
        gname = str(input('\nEmployee GNAME: ')).strip()
        sname = str(input('\nEmployee SNAME: ')).strip()
        print('')
        if x == 1 and good:
            checkin(gname, sname, storage)
        elif x == 2 and good:
            checkout(gname, sname, storage)
        elif x == 3 and good:
            print(wages(gname, sname, storage))
        elif x == 4:
            create(gname, sname, storage)
        elif not good:
            return error(nme, '14_badcsv', 'CSV file not formatted correctly or does not exist.')
        else:
            return error(nme, '15_badinput', 'Incorrect Input')
        print('\nRestart Cafe data program? (y/n)')
        if not input('  -> ').lower() == 'y':
            break
        print('')


if __name__ == '__main__':
    run()
