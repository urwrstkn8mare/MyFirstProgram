# cmdfile

import datetime
import os
import sys
import time
import random
from _21_Text2Maths import parse


# commands


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


def dice(times):
    count = ['count', 0, 0, 0, 0, 0, 0]
    show = input('Show rolls? (y/n)').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                                  'uh-huh']
    try:
        times = int(parse(times[0]))
        for l in range(times):
            x = random.randint(1, 6)
            if show:
                print(x)
            count[x] += 1
    except ValueError:
        print('You must input a correct value (integer or parsable string).')
    del count[0]
    print()
    for z in range(len(count)):
        print('Dice Roll ' + str(z + 1) + ': ' + str(count[z]) + ' times (' + str(
            (count[z] / times) * 100) + '%)')
