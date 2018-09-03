# Yr8CS1_Samit

import time
import datetime
import os
import sys

# importing projects


def prg(prgnumber):
    path = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
    find = '_' + "{0:0=2d}".format(prgnumber) + '_'
    modulepath = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i)) and \
            find in i]
    if modulepath[0] == '':
        'Could not find project.\nEnding...'
        exit()
    else:
        module = modulepath[0].split('.')
        imported = __import__(module[0])
        imported.run()
    return


# Start Up Module
def StartUp():
    global inputvar
    print('Hello! Welcome to MyFirstProgram! \n')
    print('Please project number of the project which you wish to run')
    while True:
        try:
            inputvar = int(input('-> '))
        except ValueError:
            inputvar = 'VALUEERROR'
        if isinstance(inputvar, int):
            break
        else:
            print('You must input an INTEGER. Try again...\n')
    print('\nSTARTING:')
    print('-----------------\n\n')
    start = time.time()
    nowtime = datetime.datetime.now()
    prg(int(inputvar))
    end = time.time()
    print('\n\n-----------------')
    print('Project Finished Running.')
    print('Project Runtime: ' + str(end - start) + 's - elapsed time')
    print('                 ' + str(time.process_time()) + 's - processing time')
    print('Project run at ' + str(nowtime) + '\n')
    return


if __name__ == '__main__':
    StartUp()
