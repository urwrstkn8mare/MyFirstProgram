# Yr8CS1_Samit

from CommandImportStorage import *


# importing projects


def prg(prgnumber):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
    find = '_' + "{0:0=2d}".format(prgnumber) + '_'
    modulepath = [i for i in os.listdir(path) if os.path.isfile(
        os.path.join(path, i)) and find in i]
    if not modulepath:
        print('Could not find project.\nEnding...')
        return 'NOTFOUND'
    else:
        module = modulepath[0].split('.')
        imported = __import__(module[0])
        imported.run()
    return modulepath[0]


def cmd(command):
    command = str(command).strip()
    cmds = {
        'print': cmdprint,
        'time': lambda dud: print(datetime.datetime.now()),
        'prg': lambda number: prg(int(number[0])),
        'newprg': newproject,
        'prgs': lambda duddd: prgs(),
        'delprg': delprg,
        'diceroll': dice,
        'cmds': lambda dudd: print('COMMANDS:\n' + '\n'.join(cmds)),
        'round': lambda params: print(round(float(params[0]), int(params[1]))),
        'parse': lambda param: print(parse(str(param[0]))),
        'sort': sort,
        'sort-reverse': reversesort,
        'filesort': lambda filename: filesort(filename[0]),
        'bin2dec': lambda bin_: print(bin2dec(bin_[0])),
        'bin2asc': lambda bin_: print(bin2asc(bin_[0])),
        'asc2dec': lambda asc: print(asc2dec(asc[0])),
        'asc2bin': lambda asc: print(asc2bin(asc[0])),
        'dec2bin': lambda dec: print(dec2bin(dec[0])),
        'dec2asc': lambda dec: print(dec2asc(dec[0])),
        'writefileval': lambda fle: print(writefileval(fle[0], fle[1])),
        'readfileval': lambda fle: print(readfileval(fle[0])),
        'parse': lambda input: print(parse(input[0]))
    }
    ran = False
    if '-' in command:
        command = command.strip().split('-', 1)
        commands = [str(command[0]), command[1].strip().split(',')]
        commands[1] = [xx.strip() for xx in commands[1]]
        for i in range(len(cmds)):
            ran = True
            try:
                try:
                    cmds[commands[0]](commands[1])
                except IndexError:
                    print('Not enough parameters')
                    return commands[0]
            except KeyError:
                ran = False
            if ran:
                break
    else:
        print('No seperating dash found.')
        return 'cmd-NODASH'
    if not ran:
        print('Command Not Found...')
        return 'cmd-COMMANDUNFOUND'
    else:
        return commands[0]


# Start Up Module
def startup():
    global inputvar
    print('Hello! Welcome to MyFirstProgram! \n')
    print('Please project number of the project which you wish to run')
    while True:
        inputvar = input('-> ')
        if inputvar == 'cmd':
            inputvar = 'cmd-' + input('   cmd: ')
            break
        else:
            try:
                inputvar = str(int(parse(str(inputvar))))
                break
            except ValueError:
                inputvar = 'VALUEERROR'
                print('You must input correctly. Try again...\n')
    print('\nSTARTING:')
    print('-----------------\n\n')
    start = time.time()
    nowtime = datetime.datetime.now()
    if inputvar.startswith('cmd'):
        nme = cmd(inputvar.replace('cmd-', ''))
    else:
        nme = prg(int(inputvar))
    end = time.time()
    print('\n\n-----------------')
    print('[' + nme + ']' + ' Finished Running.')
    print('Runtime: ' + str(end - start) + 's - elapsed time')
    print('         ' + str(time.process_time()) + 's - processing time')
    print('Run at ' + str(nowtime) + '\n')
    return


if __name__ == '__main__':
    startup()
