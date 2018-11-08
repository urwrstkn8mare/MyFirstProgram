# Program written by: Samit Shaikh
# Date of last revision: 20181106
# Purpose: To create functions for sorting arrays and files.

import os
from _21_Text2Maths import parse

# Imports the parse function from Project 21 and the os module from python's built-in library.

name = os.path.realpath(__file__)
# Gets the name of the file and assigns it to variable name
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
    # Turns a string into a list with each character as an individual list item.


def swap(string):
    string = str(string)
    if len(string) == 2:
        string = fullsplit(string)
        string.append(string[0])
        return ''.join(string[1:3])
    else:
        return error('03_badstrlen', 'String must be 2 characters long.', name)
    # Swaps a two character string.


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
    # If the array is not a list than the function, fullsplit, will be used to make it into an array and the variable
    #  notarray will be true (a flag).
    if len(array) <= 1:
        return list(array)
    # If the array is one list item long, then the function will return the array.

    middle = int((len(array) / 2) - 1)
    # Determines the middle of the array (or the closest to the middle).
    pivot = array[middle]
    # Assigns the middle list item of the array to the variable, pivot.
    del array[middle]
    # removes the middle item from the array.
    left, right = [], []
    # Creates an empty list assigned to variables: left and right.
    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])
        else:
            right.append(array[i])
    # For the number of list items in the array it will append it the left or right list variables depending on its
    # location relative to the pivot.
    result = quicksort(left) + [pivot] + quicksort(right)
    # creates a list variable, result, with the left, pivot and right in the list together in order.
    if notarray:
        result = ''.join(result)
    # if variable notarray (the flag) is true than to join the list together and assign it to result.
    return result
    # return variable result


def sort2(string):
    string = str(string)
    if len(string) == 2:
        if string[1] < string[0]:
            return swap(string)
        # if the right character is less than the left character than swap them.
    else:
        return error('01_badstrlen', 'String must be 2 characters long.', name)
        # if the string is not two characters long output an error


def filesort(filename, **settings):
    filename = str(filename).strip()
    # makes sure the filename is a string and possible whitespace is removed.
    default = {
        'parse': False,
        'forcestr': False,
        'newfile': True,
        'newfilename': '',
        'outputverify': True,
        'outputvalues': False
    }
    # creates a dictionary of default values for settings
    settingnames = ','.join(default).split(',')
    # creates a list containing the names of the default settings
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
    flagstring = settings['forcestr']
    for i in range(len(filecontent)):
        filecontent[i] = str(filecontent[i]).strip()
        if not flagstring:
            if settings['parse']:
                if str(parse(filecontent[i])).startswith('!ERROR'):
                    flagstring = True
            else:
                floatchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
                notfloat = True
                periodcount = 0
                for z in range(len(filecontent[i])):
                    if (str(filecontent[i])[z] in floatchars) and notfloat:
                        if str(filecontent[i]) == '.':
                            periodcount += 1
                        print('True')
                    else:
                        notfloat = False
                        print('False')
                flagstring = not notfloat
    if flagstring:
        typee = lambda value: str(value).strip()
    else:
        if settings['parse']:
            typee = lambda value: parse(value)
        else:
            typee = lambda value: float(value)
    filecontent = quicksort([typee(xx) for xx in filecontent])
    if not settings['outputvalues']:
        tempcontent = []
        for i in range(len(filecontent)):
            for b in range(len(originalcontent)):
                if filecontent[i] == typee(originalcontent[b]):
                    tempcontent.append(originalcontent[b])
        filecontent = tempcontent
    else:
        filecontent = [str(xx).strip() for xx in filecontent]
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
    elif settings['outputverify']:
        print('Cancelled, not written to new file.')


def run():
    print(quicksort('test'))
    print(quicksort(['test', 'aww', 'wow', 'wee', 'cool', '123', 'cool']))
    # filesort(str(input(': ')))
    filesort('asdfasdfa')


# Ignore below this line.


if __name__ == '__main__':
    run()
