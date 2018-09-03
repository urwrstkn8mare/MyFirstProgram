from _19_InterpreterForCSV import *
import datetime
import time

linecounterd = 1  # sets variable linecounter to 1
debugr = input('DEBUG (True/False): ')  # sets boolean logr to to user assigned bool (for logging purposes)
print()
if debugr.lower() == 'true':
    debugr = True
else:
    debugr = False


def time(tm):
    tim = str(tm).split(' ')
    halfone = tim[0].split('-')
    halftwo = tim[1].split(':')
    return [int(halfone[2]), int(halfone[1]), int(halfone[0]), int(halftwo[0]), int(halftwo[1]), float(halftwo[2])]


def debug(text, wp):
    global debugr
    global linecounterd
    if debugr:
        if wp:
            input('DEBUG>>> ' + str(text) + ' <<< ' + str(linecounterd))
        else:
            print('DEBUG>>> ' + str(text) + ' <<< ' + str(linecounterd))
        linecounterd += 1
    else:
        pass
    return text


def error(err, string):
    print(err + ' ' + string)
    input('Enter to continue...')
    return err


def create(gn, sn, storage):
    def nv(string):
        return str(input(string))

    data = read_csv(storage, True)
    try:
        strt = data[0].startswith('!ERROR')
    except AttributeError:
        strt = False
    if strt or not ', '.join(
            data[0]) == 'GNAME, SNAME, ROLE, TRATE, SUPER, HLTH, MON, TUE, WED, THU, FRI, SAT, SUN, LASTCHECKIN, LASTCHECKOUT, KEY':
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
        return error('!ERROR!', 'Incorrect ROLE input.')
    trate = nv('TRATE (30/40)').strip()
    if trate == '30' or trate == '40':
        pass
    else:
        return error('!ERROR!', 'Incorrect TRATE input.')
    superr = nv('SUPER (4/6/8)').strip()
    if superr == '4' or superr == '6' or superr == '8':
        pass
    else:
        return error('!ERROR!', 'Incorrect SUPER input.')
    hlth = nv('HLTH (15/25/45)').strip()
    if hlth == '15' or hlth == '25' or hlth == '45':
        pass
    else:
        return error('!ERROR!', 'Incorrect HLTH input.')
    data = read_csv(storage, True)
    key = str(len(data))
    append_csv_record(storage,
                      [gn, sn, role, trate, superr, hlth, 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a',
                       'n/a', key])
    print('CREATED NEW USER DATA')


def checkin(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if test1 == test2 and not test1 == None and not test2 == None:
        sett = find_csv_record(storage, gn, key='GNAME')
        now = str(datetime.datetime.now())
        update_csv_record(storage, True, int(sett['KEY']), 'LASTCHECKIN', now)
        print('CHECKED IN AT ' + now)
    else:
        return error('!ERROR_NOT_FOUND!', 'Could not find given name and username.')


def checkout(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if test1 == test2 and not test1 == None and not test2 == None:
        sett = find_csv_record(storage, gn, key='GNAME')
        now = str(datetime.datetime.now())
        update_csv_record(storage, True, int(sett['KEY']), 'LASTCHECKOUT', now)
        debug('THIS DEBUG PAUSE TIME ALLOWS YOU TO CHANGE CSV DATA', True)
        sett = find_csv_record(storage, gn, key='GNAME')
        if time(sett['LASTCHECKOUT'])[2] == time(sett['LASTCHECKIN'])[2]:
            weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
            timee = time(sett['LASTCHECKOUT'])[3] - time(sett['LASTCHECKIN'])[3]
            day = int(datetime.datetime.today().weekday())
            if timee < 0:
                return error('!ERROR!', 'Y' + 'OU CANNOT WORK PAST A DAY.'.lower())
            for m in range(7 - day):
                update_csv_record(storage, True, int(sett['KEY']), weekday[day + m], 'n/a')
            update_csv_record(storage, True, int(sett['KEY']), weekday[day], str(timee))
        print('CHECKED OUT AT ' + now)
    else:
        return error('!ERROR_NOT_FOUND!', 'Could not find given name and username.')


def wages(gn, sn, storage):
    test1 = find_csv_record(storage, gn, key='GNAME')
    test2 = find_csv_record(storage, sn, key='SNAME')
    if test1 == test2 and not test1 == None and not test2 == None:
        sett = find_csv_record(storage, gn, key='GNAME')
        weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
        wage = 0
        if sett['ROLE'].lower() == 'barista':
            rate = 23
        elif sett['ROLE'].lower() == 'manager':
            rate = 30
        else:
            return error('!ERROR_CORRUPT!', 'Incorrectly filled role data.')
        debug('role: ' + str(sett['ROLE']), True)
        for i in range(len(weekday)):
            if not sett[weekday[i]] == 'n/a':
                debug(i, True)
                try:
                    if 0 < int(sett[weekday[i]]) - 9 <= 3 and i <= 4:
                        wagetmp = (9 * rate) + (((int(sett[weekday[i]]) - 9) * rate) * (125/100))
                    elif int(sett[weekday[i]]) - 9 > 3 and i <= 4:
                        wagetmp = (9 * rate) + (((int(sett[weekday[i]]) - 9) * rate) * (145/100))
                    elif i == 5 and int(sett[weekday[i]]) <= 9:
                        wagetmp = int(sett[weekday[i]]) * (rate + 3)
                    elif i == 6 and int(sett[weekday[i]]) <= 9:
                        wagetmp = int(sett[weekday[i]]) * (rate + 4)
                    elif int(sett[weekday[i]]) - 9 > 0 and i == 5:
                        wagetmp = (9 * (rate + 3)) + (((int(sett[weekday[i]]) - 9) * rate) * (150/100))
                    elif int(sett[weekday[i]]) - 9 > 0 and i == 6:
                        wagetmp = (9 * (rate + 4)) + (((int(sett[weekday[i]]) - 9) * rate) * (150/100))
                    elif int(sett[weekday[i]]) <= 9 and i <= 4:
                        wagetmp = int(sett[weekday[i]]) * rate
                    else:
                        return error('!ERROR!', 'Problem with validating pay rates.')
                    debug('wagetmp: ' + str(wagetmp), True)
                except ValueError:
                    return error('!ERROR_CORRUPT_2!', 'Incorrectly filled hour data.')
            else:
                return error('!ERROR!', 'All working hours not defined.')
            wage = wage + wagetmp
        super = int(sett['SUPER'])
        debug('super: ' + str(super), True)
        hlth = int(sett['HLTH'])
        debug('hlth: ' + str(hlth), True)
        tax = int(sett['TRATE'])
        debug('tax: ' + str(tax), True)
        debug('wage: ' + str(wage), True)
        debug('final: ' + str(((wage * (100 - super) / 100) - hlth) * (100 - tax) / 100), True)
        return ((wage * (100 - super) / 100) - hlth) * (100 - tax) / 100
    else:
        return error('!ERROR_NOT_FOUND!', 'Could not find given name and username.')


def run():
        while True:
            storage = input('CSV Data: ')
            print('!NOTE! This program stores information in ' + storage + '.\nWelcome to Cafe')
            print('Please choose your action: ')
            print('     1 - Check In')
            print('     2 - Check Out')
            print('     3 - Calculate Wages')
            print('     4 - Create Employee Data')
            try:
                x = int(input('  -> '))
            except ValueError:
                error('!ERROR_1!', 'Incorrect Input')
                x = 0
            gname = str(input('\nEmployee GNAME: ')).strip()
            sname = str(input('\nEmployee SNAME: ')).strip()
            print('')
            if x == 1:
                checkin(gname, sname, storage)
            elif x == 2:
                checkout(gname, sname, storage)
            elif x == 3:
                print(wages(gname, sname, storage))
            elif x == 4:
                create(gname, sname, storage)
            else:
                error('!ERROR_2!', 'Incorrect Input')
            print('\nRestart Cafe data program? (y/n)')
            if not input('  -> ').lower() == 'y':
                break
            print('')


if __name__ == '__main__':
    run()
