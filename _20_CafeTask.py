from _19_InterpreterForCSV import *

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

    data = Read_csv(storage, True)
    if data[0].startswith('!ERROR') or not ', '.join(data[0]) == 'GNAME, SNAME, ROLE, TRATE, SUPER, HLTH, MON, TUE, WED, THU, FRI, SAT, SUN, LASTCHECKIN, LASTCHECKOUT':
        write_csv_record(storage, [
            ['GNAME', 'SNAME', 'ROLE', 'TRATE', 'SUPER', 'HLTH', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN',
             'LASTCHECKIN', 'LASTCHECKOUT']])
    print('Please enter the information for ' + gn + ' ' + sn + '.')
    role = nv('ROLE (Barista/Manager): ').strip()
    role = role.lower()
    if role == 'barista' or role == 'manager':
        pass
    else:
        error('!ERROR! Incorrect ROLE input.')
    trate = nv('TRATE (30/40)').strip()
    if trate == '30' or trate == '40':
        pass
    else:
        error('!ERROR! Incorrect TRATE input.')
    trate = nv('TRATE (4/6/8)').strip()
    if trate == '4' or trate == '6' or 8 :
        pass
    else:
        error('!ERROR! Incorrect TRATE input.')
    append_csv_record(storage, [gn, sn, role, trate, superr, hlth, mon, tue, wed, thu, fri, sat, sun, lastcheckin, lastcheckout])


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
    gname = str(input('\nEmployee GNAME: '))
    sname = str(input('\nEmployee SNAME: '))
    if x == 1:
        print(checkin(gname, sname, storage))
    elif x == 2:
        print(checkout(gname, sname, storage))
    elif x == 3:
        print(wages(gname, sname, storage))
    elif x == 4:
        print(create(gname, sname, storage))
    else:
        error('!ERROR_2!', 'Incorrect Input')


if __name__ == '__main__':
    run()
