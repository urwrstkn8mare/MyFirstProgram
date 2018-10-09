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
    if not modulepath:
        print('Could not find project.\nEnding...')
        return 'NOTFOUND'
    else:
        module = modulepath[0].split('.')
        imported = __import__(module[0])
        imported.run()
    return modulepath[0]


# cmdfile

def cmd():
    def cmdprint(order):
        order = str(order[0])
        print(str(order))

    def newproject(title):
        title = str(title[0])
        template = '#Created ' + str(datetime.datetime.now()) + '\n#' + title + '\n\n\ndef run():\n    \"\"' \
                                                                                '\"\n    Mainline code goes in the' \
                                                                                ' below, any functions, imports or' \
                                                                                ' global variables can go outside ' \
                                                                                'as long as\n    this is the code ' \
                                                                                'that is meant to run.\n    \"\"\"' \
                                                                                '\n\n# Ignore below this line.\n\n\nif' \
                                                                                ' __name__ == \'__main__\':\n    r' \
                                                                                'un()\n'
        z = 0
        while True:
            path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
            find = '_' + "{0:0=2d}".format(z) + '_'
            modulepath = [l for l in os.listdir(path) if os.path.isfile(os.path.join(path, l)) and find in l]
            if not modulepath:
                break
            else:
                z += 1
        with open('_' + "{0:0=2d}".format(z) + '_' + title + '.py', 'w+') as f:
            f.write(template)
        f.close()

    def delprg(prgnumber):
        prgnumber = int(prgnumber[0])
        path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
        find = '_' + "{0:0=2d}".format(prgnumber) + '_'
        modulepath = [l for l in os.listdir(path) if os.path.isfile(os.path.join(path, l)) and find in l]
        if not modulepath:
            print('Could not find project.\nEnding...')
            return 'NOTFOUND'
        else:
            os.remove(str(modulepath[0]))

    def prgs():
        z = 0
        files = []
        while True:
            path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
            find = '_' + "{0:0=2d}".format(z) + '_'
            modulepath = [l for l in os.listdir(path) if os.path.isfile(os.path.join(path, l)) and find in l]
            if not modulepath:
                break
            else:
                files.append(modulepath[0])
                z += 1
        print('MyFirstProgram')
        for h in range(len(files)):
            print(' -->' + str(files[h]))

    command = str(input('\n   cmd: ')).strip()
    print('-----------------\n\n')
    cmds = {
        'print': cmdprint,
        'time': lambda dud: print(datetime.datetime.now()),
        'prg': lambda number: prg(int(number[0])),
        'newprg': newproject,
        'prgs': lambda dud: prgs(),
        'delprg': delprg
    }
    end = 0
    start = 0
    nowtime = 0
    ran = False
    if '-' in command:
        command = command.strip().split('-', 1)
        commands = [str(command[0]), command[1].strip().split(',')]
        for i in range(len(cmds)):
            ran = True
            try:
                start = time.time()
                nowtime = datetime.datetime.now()
                try:
                    cmds[commands[0]](commands[1])
                except IndexError:
                    print('\n\n-----------------\nNot enough parameters')
                    return
                end = time.time()
            except KeyError:
                ran = False
            if ran:
                break
    else:
        print('\n\n-----------------\nNo seperating dash found.')
        return
    print('\n\n-----------------')
    if not ran:
        print('Command Not Found...')
    else:
        print('[' + commands[0] + ']' + ' Finished Running.')
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
