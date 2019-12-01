# Written by: Samit Shaikh
# Date of last Revision: 26062018
# Purpose: to find and report differences in two input files

import os
import platform
import file


def diff(line1, line2):
    global numberof

    def addpspace(item, no):
        while len(item) < no + 1:
            item = item + ' '
        return item

    if len(line1) < len(line2):
        line1 = addpspace(line1, len(line2))
        numberof = len(line2)
    elif len(line2) < len(line1):
        line2 = addpspace(line2, len(line1))
        numberof = len(line1)
    else:
        numberof = len(line1)
    ii = 0
    dif = []
    dif1 = ''
    dif2 = ''
    while ii < numberof:
        if line1[ii] == line2[ii]:
            dif.append(True)
            dif1 = dif1 + '\033[42;30m' + line1[ii] + '\033[m'
            dif2 = dif2 + '\033[42;30m' + line2[ii] + '\033[m'
        else:
            dif.append(False)
            dif1 = dif1 + '\033[41;30m' + line1[ii] + '\033[m'
            dif2 = dif2 + '\033[41;30m' + line2[ii] + '\033[m'
        ii += 1
    return [dif, dif1, dif2]


def main():
    if platform.system() == 'Linux' or 'Darwin':
        pass
    else:
        print('Platform unsupported yet.')
        input()
        exit()

    while True:
        print('Welcome to Difference Finder!')
        print('')
        ask = int(input('Do you want to enter your own lines or read off a .txt document?'
                        ' (1/2) '))
        print('')
        if ask == 1:
            print('Start typing you lines for \'a\' a below: ')
            print(
                'NOTE>>> to finish, just enter the new line without writing anything in the line.'
                ' (the line will automatically be removed.)')
            print('')
            n = 1
            a = []
            while True:
                a.append(input('a' + str(n) + '     '))
                if a[n - 1] == '':
                    del a[n - 1]
                    break
                else:
                    n += 1
            print('')
            print('Start typing you lines for \'b\' a below: ')
            print(
                'NOTE>>> to finish, just enter the new line without writing anything in the line.'
                ' (the line will automatically be removed.)')
            print('')
            n = 1
            b = []
            while True:
                b.append(input('b' + str(n) + '     '))
                if b[n - 1] == '':
                    del b[n - 1]
                    break
                else:
                    n += 1
        else:
            a = input('File a: ')
            b = input('File b: ')
            print('Reading file a...')
            a = file.read(a, 0)
            print('Reading file b...')
            b = file.read(b, 0)
        if len(a) < len(b):
            while True:
                a.append('')
                if len(a) < len(b):
                    pass
                else:
                    break
        elif len(b) < len(a):
            while True:
                b.append('')
                if len(b) < len(a):
                    pass
                else:
                    break
        else:
            pass
        print('')
        print('Differences: ')
        print('')
        diff(a, b)
        print('')
        print('!DONE!')
        print('')
        return


def run():
    main()

    while True:
        restart = input('Restart? (y/n) ')
        if restart.lower() == 'y':
            print('Restarting...')
            print('')
            main()
        elif restart.lower() == 'n':
            print('Ending...')
            break
        else:
            print('Unknown Response. Ending...')
            break


if __name__ == '__main__':
    run()
