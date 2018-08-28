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


def run():
    print('Welcome to Cafe')
    print('Please choose your action: ')
    print('     1 - Check In')
    print('     2 - Check Out')
    print('     3 - Calculate Wages')
    print('     4 - Update Employee Data')
    print('     5 - Create Employee Data')
    try:
        x = int(input('  -> '))
    except:
        error('!ERROR_1!', 'Incorrect Input')
    gname = str(input('\nEmployee GNAME: '))
    sname = str(input('\nEmployee SNAME: '))
    if x == 1:
        print(checkin(gname, sname))
    elif x == 2:
        print(checkout(gname, sname))
    elif x == 3:
        print(wages(gname, sname))
    elif x == 4:
        print(update(gname, sname))
    elif x == 5:
        print(create(gname, sname))
    else:
        error('!ERROR_2!', 'Incorrect Input')


if __name__ == '__main__':
    run()