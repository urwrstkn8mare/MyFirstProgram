"""
Created 2018-10-09 11:51:24.501005
SortString
"""
import os
from _21_Text2Maths import parse

name = os.path.realpath(__file__)
logs = input('LOGS (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                                'uh-huh']  # If userinput is in the list then variable logr is True
print()  # Print new line


def log(text, validator, **opt):
    # This function accepts parameters: text, validator and 2 optional parameters.
    namee = ''
    # Initialise name with an empty string.
    if 'name' in opt:
        namee = opt['name']
    # If user did assign a value to the optional parameter, 'name', then the value would be stored in variable name.
    if validator:
        if 'wait' in opt:
            if opt['wait']:
                input('LOG>>> Enter to continue >>>')
            else:
                print('LOG>>> ' + str(text) + ' <<< ' + str(namee))
        else:
            print('LOG>>> ' + str(text) + ' <<< ' + str(namee))
    # If validator is True (normally this is used so when they run the program they can choose if they want logging
    # or not.) then a string with the text and name used in it will be printed unless it is specified that the user
    # enter's to continue. This can be specified in optional paramter, 'wait' with the value: True.


def error(err, string, nameee):
    # This function will return the error name that programs can use and print a error message in the console.
    print('\n!ERROR_' + err.upper() + '! ' + string + ' [' + nameee + ']\n')
    return '!ERROR_' + err.upper() + '!'


def fullsplit(string):
    new = []
    for z in range(len(string)):
        new.append(string[z])
    return new


def swap(string):
    string = str(string)
    if len(string) == 2:
        string = fullsplit(string)
        string.append(string[0])
        return ''.join(string[1:3])
    else:
        return error('03_badstrlen', 'String must be 2 characters long.', name)


def sortall(string):
    # first sorting algorithm without any knowledge of the algorithms
    string = str(string)
    letter = fullsplit(string.lower() + ' ')
    alphabet = fullsplit('abcdefghijklmnopqrstuvwxyz')
    done = []
    for i in range(len(alphabet)):
        log(letter, logs, name='letter')
        for n in range(len(letter)):
            log(letter[n] + '=' + alphabet[i] + '(' + str(n) + ')', logs)
            if letter[n] == alphabet[i]:
                done.append(string[n])
    return ''.join(done)


def quicksort(array):
    # made thyis myself btw
    notarray = False
    if not isinstance(array, list):
        array = fullsplit(array)
        notarray = True
    if len(array) <= 1:
        return list(array)

    middle = int((len(array) / 2) - 1)
    pivot = array[middle]
    del array[middle]
    left = []
    right = []
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    result = quicksort(left) + [pivot] + quicksort(right)
    if notarray:
        result = ''.join(result)
    return result


def sort2(string):
    string = str(string)
    if len(string) == 2:
        if string[1] < string[0]:
            return swap(string)
    else:
        return error('01_badstrlen', 'String must be 2 characters long.', name)


def sort3(string):
    string = str(string)
    if len(string) == 3:
        return sortall(string)
    else:
        return error('02_badstrlen', 'String must be 3 characters long.', name)


def filesort(filename, **settings):
    filename = str(filename).strip()
    default = {
        'parse': False,
        'forcestr': False,
        'newfile': True,
        'newfilename': '',
        'outputverify': True,
        'outputvalues': False
    }
    settingnames = ','.join(default).split(',')
    boolexceptions = ['newfilename']
    for x in range(len(settingnames)):
        if not settingnames[x] in settings:
            settings[settingnames[x]] = str(default[settingnames[x]])
        if not settingnames[x] in boolexceptions:
            settings[settingnames[x]] = str(settings[settingnames[x]]).lower() in ['true', '1', 't', 'y', 'yes', 'yeah',
                                                                                   'yup', 'certainly',
                                                                                   'uh-huh']
    try:
        with open(str(filename)) as fr:
            filecontent = fr.readlines()
            originalcontent = [str(xx).strip() for xx in filecontent]
            fr.close()
    except FileNotFoundError:
        return error('04_filenotfound', str('The file [' + str(filename) + '] was not found.'), name)
    if settings['forcestr']:
        flagstring = True
    else:
        flagstring = False
    for i in range(len(filecontent)):
        filecontent[i] = str(filecontent[i]).strip()
        if not flagstring:
            if settings['parse']:
                if str(parse(filecontent[i])).startswith('!ERROR'):
                    flagstring = True
            else:
                try:
                    float(filecontent[i])
                except ValueError:
                    flagstring = True
    if flagstring:
        filecontent = [str(xx).strip() for xx in filecontent]
    else:
        if settings['parse']:
            filecontent = [parse(xx) for xx in filecontent]
        else:
            filecontent = [float(xx) for xx in filecontent]
    filecontent = quicksort(filecontent)
    if not settings['outputvalues']:
        tempcontent = []
        for i in range(len(filecontent)):
            for b in range(len(originalcontent)):
                if flagstring:
                    if filecontent[i] == str(originalcontent[b]):
                        tempcontent.append(originalcontent[b])
                else:
                    if settings['parse']:
                        if filecontent[i] == parse(originalcontent[b]):
                            tempcontent.append(originalcontent[b])
                    else:
                        if filecontent[i] == float(originalcontent[b]):
                            tempcontent.append(originalcontent[b])
    else:
        tempcontent = [str(xx).strip() for xx in filecontent]
    if settings['outputverify']:
        print('\nNew Sorted File: \n    ' + '\n    '.join(filecontent) + '\n[WRITE] OR [CANCEL]')
        verify = str(input('       ')).lower() in ['write', 'w']
    else:
        print()
        verify = True
    if verify:
        if settings['newfile']:
            if settings['newfilename'] == '':
                newfilename = filename.split('.')
                newfilename = ''.join(newfilename[:-1]) + 'sorted.' + newfilename[-1]
            else:
                newfilename = str(settings['newfilename'])
        else:
            newfilename = filename
        f = open(str(newfilename), 'w+')
        f.write('\n'.join(filecontent))
        f.close()
        if settings['outputverify']:
            print('New Sorted File written to: ' + str(newfilename))
    else:
        if settings['outputverify']:
            print('Cancelled, not written to new file.')


def run():
    print(quicksort('test'))
    print(quicksort(['test', 'aww', 'wow', 'wee', 'cool', '123', 'cool']))
    # filesort(str(input(': ')))


# Ignore below this line.


if __name__ == '__main__':
    run()
