# Yr8CS1_Samit

import time
import datetime
import os
import sys
from _21_Text2Maths import parse


# importing projects


def prg(prgnumber):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
    find = '_' + "{0:0=2d}".format(prgnumber) + '_'
    modulepath = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i)) and find in i]
    if modulepath[0] == '':
        print('Could not find project.\nEnding...')
        exit()
    else:
        module = modulepath[0].split('.')
        imported = __import__(module[0])
        imported.run()
    return modulepath[0]


# cmdline
def cmd():
    def cmdprint():
        print(input('PRINT: '))

    command = str(input('\nCMD: ')).strip()
    print('-----------------\n\n')
    cmds = {
        'print': cmdprint,
        'time': lambda: print(datetime.datetime.now())
    }
    end = 0
    start = 0
    nowtime = 0
    for i in range(len(cmds)):
        ran = True
        try:
            start = time.time()
            nowtime = datetime.datetime.now()
            cmds[command]()
            end = time.time()
        except KeyError:
            ran = False
        if ran:
            break
        print('\n\n-----------------')
    if not ran:
        print('Command Not Found...')
    else:
        print('[' + command + ']' + ' Finished Running.')
        print('Runtime: ' + str(end - start) + 's - elapsed time')
        print('         ' + str(time.process_time()) + 's - processing time')
        print('Run at ' + str(nowtime) + '\n')


# Start Up Module
def startup():
    global inputvar
    print('Hello! Welcome to MyFirstProgram! \n')
    print('Please project number of the project which you wish to run')
    while True:
        inputvar = input('-> ')
        if inputvar == 'cmd':
            return cmd()
        else:
            try:
                inputvar = int(parse(str(inputvar)))
            except ValueError:
                inputvar = 'VALUEERROR'
            if isinstance(inputvar, int):
                break
            else:
                print('You must input correctly. Try again...\n')
    print('\nSTARTING:')
    print('-----------------\n\n')
    start = time.time()
    nowtime = datetime.datetime.now()
    name = prg(int(inputvar))
    end = time.time()
    print('\n\n-----------------')
    print('[' + name + ']' + ' Finished Running.')
    print('Runtime: ' + str(end - start) + 's - elapsed time')
    print('         ' + str(time.process_time()) + 's - processing time')
    print('Run at ' + str(nowtime) + '\n')
    return


if __name__ == '__main__':
    startup()
