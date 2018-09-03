from _19_InterpreterForCSV import *
import datetime
import time

linecounter = 1  # sets variable linecounter to 1
logr = input('LOG (True/False): ')  # sets boolean logr to to user assigned bool (for logging purposes)
print()
if logr.lower() == 'true':
    logr = True
else:
    logr = False


def time(tm):
    tim = str(tm).split(' ')
    halfone = tim[0].split('-')
    halftwo = tim[1].split(':')
    return [int(halfone[2]), int(halfone[1]), int(halfone[0]), int(halftwo[0]), int(halftwo[1]), float(halftwo[2])]


def log(text):
    global logr
    global linecounter
    if logr:
        print('LOG>>> ' + str(text) + ' <<< ' + str(linecounter))
        linecounter += 1
    else:
        pass
    return


def error(err, string):
    print(err + ' ' + string)
    input('Enter to continue...')
    return err


def name2numb(gn, sn, storage):
    result = False
    set = read_csv(storage, True)
    for i in range(len(set)):
        if set[i]['GNAME'].lower() == gn.lower() and set[i]['SNAME'].lower() == sn.lower():
            result = i
    if not result:
        error('!ERROR!', 'Could not find row assigned to name.')
    return result


def create(gn, sn, storage):
    def nv(string):
        return str(input(string))

    data = read_csv(storage, True)
    if data[0].startswith('!ERROR') or not ', '.join(
            data[0]) == 'GNAME, SNAME, ROLE, TRATE, SUPER, HLTH, MON, TUE, ' \
                        'WED, THU, FRI, SAT, SUN, LASTCHECKIN, LASTCHECKOUT':
        print('CREATING NEW DATA CSV')
        write_csv_record(storage, [
            ['GNAME', 'SNAME', 'ROLE', 'TRATE', 'SUPER', 'HLTH', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN',
             'LASTCHECKIN', 'LASTCHECKOUT']])
    print('\nPlease enter the information for ' + gn + ' ' + sn + '.')
    role = nv('ROLE (Barista/Manager): ').strip()
    role = role.lower()
    if role == 'barista' or role == 'manager':
        pass
    else:
        error('!ERROR!', 'Incorrect ROLE input.')
    trate = nv('TRATE (30/40)').strip()
    if trate == '30' or trate == '40':
        pass
    else:
        error('!ERROR!', 'Incorrect TRATE input.')
    superr = nv('SUPER (4/6/8)').strip()
    if superr == '4' or superr == '6' or superr == '8':
        pass
    else:
        error('!ERROR!', 'Incorrect SUPER input.')
    hlth = nv('HLTH (15/25/45)').strip()
    if hlth == '15' or hlth == '25' or hlth == '45':
        pass
    else:
        error('!ERROR!', 'Incorrect HLTH input.')
    append_csv_record(storage,
                      [gn, sn, role, trate, superr, hlth, 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a',
                       'n/a'])
    print('CREATED NEW USER DATA')


def checkin(gn, sn, storage):
    row = name2numb(gn, sn, storage)
    update_csv_record(storage, True, row, 'LASTCHECKIN', str(datetime.datetime.now()))


def checkout(gn, sn, storage):
    row = name2numb(gn, sn, storage)
    sett = read_csv(storage, True)
    update_csv_record(storage, True, row, 'LASTCHECKOUT', str(datetime.datetime.now()))
    weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    timee = time(sett[row]['LASTCHECKOUT'])[3] - time(sett[row]['LASTCHECKIN'])[3]
    day = int(datetime.datetime.today().weekday())
    if timee < 0:
        error('!ERROR!', 'Y' + 'OU CANNOT WORK PAST A DAY.'.lower())
    for m in range(7 - day):

    update_csv_record(storage, True, row, weekday[day], str(time))


def run():
    storage = 'cafedata.csv'
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
    gname = str(input('\nEmployee GNAME: '))
    sname = str(input('\nEmployee SNAME: '))
    if x == 1:
        print(checkin(gname, sname, storage))
    elif x == 2:
        print(checkout(gname, sname, storage))
    elif x == 3:
        print(wages(gname, sname, storage))
    elif x == 4:
        create(gname, sname, storage)
    else:
        error('!ERROR_2!', 'Incorrect Input')


if __name__ == '__main__':
    print(time(datetime.datetime.now()))
