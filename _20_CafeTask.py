from _19_InterpreterForCSV import *
import datetime
import time


def elapsed_interval(start, end):
    elapsed = end - start
    min, secs = divmod(elapsed.days * 86400 + elapsed.seconds, 60)
    hour, minutes = divmod(min, 60)
    return '%.2d:%.2d:%.2d' % (hour, minutes, secs)


linecounter = 1  # sets variable linecounter to 1
logr = input('LOG (True/False): ')  # sets boolean logr to to user assigned bool (for logging purposes)
print()
if logr.lower() == 'true':
    logr = True
else:
    logr = False


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


def create(gn, sn, storage):
    def nv(string):
        return str(input(string))

    data = read_csv(storage, True)
    if data[0].startswith('!ERROR') or not ', '.join(
            data[0]) == 'KEY, GNAME, SNAME, ROLE, TRATE, SUPER, HLTH, MON, TUE, ' \
                        'WED, THU, FRI, SAT, SUN, LASTCHECKIN, LASTCHECKOUT':
        print('CREATING NEW DATA CSV')
        write_csv_record(storage, [
            ['KEY', 'GNAME', 'SNAME', 'ROLE', 'TRATE', 'SUPER', 'HLTH', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN',
             'LASTCHECKIN', 'LASTCHECKOUT']])
    newdata = read_csv(storage, True)
    key = "{0:0=3d}".format(int(newdata[len(newdata) - 1]['KEY']) + 1)
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
                      [key, gn, sn, role, trate, superr, hlth, 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a', 'n/a',
                       'n/a'])
    print('CREATED NEW USER DATA')


def checkin(gn, sn, storage):
    update_csv_record(storage, True, 1, 'LASTCHECKIN', str(datetime.datetime.now()))


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
    time_start = str(datetime.datetime.now())
    print(time_start)
    """time.sleep(5)
    time_end = float(str(datetime.hour()))
    total_time = elapsed_interval(time_start, time_end)
    print(total_time)"""
