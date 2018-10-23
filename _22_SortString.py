"""
Created 2018-10-09 11:51:24.501005
SortString
"""
import os

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
    # If validator is True (normally this is used so when they run the program they can choose if they want logging or
    # not.) then a string with the text and name used in it will be printed unless it is specified that the user enter's to continue.
    # This can be specified in optional paramter, 'wait' with the value: True.


def error(nameee, err, string):
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


def sort2(string):
    string = str(string)
    if len(string) == 2:
        return sortall(string)
    else:
        return error('01_badstrlen', 'String must be 2 characters long.', name)


def sort3(string):
    string = str(string)
    if len(string) == 3:
        return sortall(string)
    else:
        return error('02_badstrlen', 'String must be 3 characters long.', name)


def quicksort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return str(''.join(fullsplit(less) + pivotList + fullsplit(more)))


def run():
    strinput = input(': ')
    print(swap(strinput))
    print(''.join(sorted(strinput)))
    print(sortall(strinput))
    print(quicksort(strinput))


# Ignore below this line.


if __name__ == '__main__':
    run()
