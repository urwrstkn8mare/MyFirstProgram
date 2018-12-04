# Program written by: Samit Shaikh
# Date of last revision: 20181106
# Purpose: To create functions for sorting arrays and files.

import os

# Imports the os module from python's built-in library

pathname = os.path.realpath(__file__)
# Gets the name of the file and assigns it to variable name
logs = input('LOGS (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                                'uh-huh']
# Variable logs is set to true as long as the input is in the list of valid inputs.

print()


# Print new line


def log(text, validator, **opt):
    # This function accepts parameters: text, validator and 2 optional parameters. The purpose of this is to provide a
    # method of logging, at the user of the program's discretion, that is distinguishable from the rest of the normal
    # output.
    name = ''
    # Create a variable, namee, containing an empty string.
    if 'name' in opt:
        name = opt['name']
    # If the optional parameter, name, is defined then the parameter is assigned to variable namee.
    if validator:
        # If the parameter, validator, is True, then run the rest of the program.
        if not text == '':
            print('LOG>>> ' + str(text) + ' <<< ' + str(name))
            # If the text parameter is not empty then print the variable contents sandwiched in 'log' and arroT4 Alg Prac Test Q6.py
            # sorted.txt
            # unsorted.txtws to
            # differentiate from the normal output.
        if 'wait' in opt:
            # If the optional parameter, wait, then run the following code.
            if opt['wait']:
                input('LOG>>> Enter to continue >>>')
            # If the optional parameter, wait, is True then wait for the user to let the program continue.


def error(err, string, nameee):
    # This function will return the error name that programs can use and print a error message in the console.
    print('\n!ERROR_' + err.upper() + '! ' + string + ' [' + nameee + ']\n')
    return '!ERROR_' + err.upper() + '!'


def fullsplit(string):
    new = []
    for z in range(len(string)):
        new.append(string[z])
        # Iteratively adds each character as an individual list item to a list.
    return new
    # Turns a string into a list with each character as an individual list item.


def swap(string):
    string = str(string)
    if len(string) == 2:
        string = fullsplit(string)
        string.append(string[0])
        return ''.join(string[1:3])
    else:
        return error('03_badstrlen', 'String must be 2 characters long.', pathname)
    # Swaps two characters in a two character string.


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


def quicksort(array, **opt):
    # made thyis myself btw, after learning about different algorithms. My first recursive algorithm! In this case,
    # I think a recursive algorithm is stable. I am not quite sure how to implement it in iterative yet.
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
        if 'reverse' in opt:
            if opt['reverse']:
                if array[i] > pivot:
                    left.append(array[i])
                else:
                    right.append(array[i])
            else:
                if array[i] < pivot:
                    left.append(array[i])
                else:
                    right.append(array[i])
        else:
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
        return error('01_badstrlen', 'String must be 2 characters long.', pathname)
        # if the string is not two characters long output an error


def filesort(filename, **settings):
    filename = str(filename).strip()
    # makes sure the filename is a string and possible whitespace is removed.
    default = {
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
    # a list of setting names that are not to be turned to a bool
    for x in range(len(settingnames)):
        if not settingnames[x] in settings:
            settings[settingnames[x]] = str(default[settingnames[x]])
        if not settingnames[x] in boolexceptions:
            settings[settingnames[x]] = str(settings[settingnames[x]]).lower() in ['true', '1', 't', 'y', 'yes', 'yeah',
                                                                                   'yup', 'certainly',
                                                                                   'uh-huh']
        # For each setting it checks if it has been defined as an optional paramter, if not it uses the default value
        # defined previousely. Then, if it is not in boolexceptions, it makes each settings into true as long as it is
        # in the list.
    try:
        with open(str(filename)) as fileread:
            filecontent = fileread.readlines()
            filecontent = [str(xx).strip() for xx in filecontent]
            originalcontent = [str(xx).strip() for xx in filecontent]
            fileread.close()
    except FileNotFoundError:
        return error('04_filenotfound', str('The file [' + str(filename) + '] was not found.'), pathname)
    # Tries to open and read the file which name is contained in variable, filename. Then it strips each line of
    # whitespace before closing the file. If a FileNotFoundError is outputted it handles it and outputs a custom
    # error so it doesnt't stop the whole program. Also creates an identical to filecontent, originalcontent variable.
    flagstring = settings['forcestr']
    # Variable flagstring is created with the value of 'forcestr' of the dictionary, settings.
    for line in range(len(filecontent)):
        # For every item in list, filecontent, run the following.
        if not flagstring:
            # If flagstring is False, then run the following.
            floatchars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
            # List with all allowed characters in a float as an individual item
            notfloat = True
            periodcount = 0
            # Ininitialising notfloat with True and periodcount with 0
            for z in range(len(filecontent[line])):
                if (str(filecontent[line])[z] in floatchars) and notfloat:
                    if str(filecontent[line]) == '.':
                        periodcount += 1
                        if periodcount > 1:
                            notfloat = False
                else:
                    notfloat = False
            flagstring = not notfloat
            # checks for every character if it is is the allowed character. Also it checks if there is only one period.
            # Won't continue checking if it is already false.
    if flagstring:
        typee = lambda value: str(value).strip()
        # If flagstring is True, then a lambda function is created that turns the parameter into a string and strips it.
    else:
        typee = lambda value: float(value)
        # If flagstring is False, then a lambda function is created that turns the parameter into a float.
    filecontent = quicksort([typee(line) for line in filecontent])
    # Quicksorts the converted lines and
    if not settings['outputvalues']:
        tempcontent = []
        for line in range(len(filecontent)):
            for oline in range(len(originalcontent)):
                if filecontent[line] == typee(originalcontent[oline]):
                    tempcontent.append(originalcontent[oline])
        filecontent = tempcontent
        # If 'outputvalues' of dictionary, settings, is False then for every line in the sorted array find the matching
        # line in the original array and append it to temp content.
    else:
        filecontent = [str(line).strip() for line in filecontent]
        # Else, turn filecontent back into a string and strip it.
    if settings['outputverify']:
        print('\nNew Sorted File: \n    ' + '\n    '.join(filecontent) + '\n[WRITE] OR [CANCEL]')
        verify = str(input('       ')).lower() in ['write', 'w']
        # If 'outputverify' of settings is True, then print the new file and ask the user to confirm or cancel.
    else:
        print()
        verify = True
        # If not, verify is set to True.
    if verify:
        # If verify is True then run the following.
        if settings['newfile']:
            # If 'newfile' of dictionary, settings, is True then run the following.
            if settings['newfilename'] == '':
                newfilename = filename.split('.')
                newfilename = ''.join(newfilename[:-1]) + 'sorted.' + newfilename[-1]
                # If 'newfilename' of dictionary, settings, is empty, then autocreate a new one and assign it to
                # newfilename.
            else:
                newfilename = str(settings['newfilename'])
                # Else assign the value of 'newfilename' of settings to newfilename

        else:
            newfilename = filename
            # Else, assign filename to newfilename
        file = open(str(newfilename), 'w+')
        file.write('\n'.join(filecontent))
        file.close()
        # Overwrite/create a file which name is stored in newfilename.
        if settings['outputverify']:
            print('New Sorted File written to: ' + str(newfilename))
            # If 'outputverify' of settings is true, then print out the newname with a message confirming write.
    elif settings['outputverify']:
        print('Cancelled, not written to new file.')
        # If 'outputverify' of settings is False, then print out a message confirming cancel.


def run():
    print(quicksort('test'))
    print(quicksort(['test', 'aww', 'wow', 'wee', 'cool', '123', 'cool']))
    # filesort(str(input(': ')))
    filesort('asdfasdfa')


# Ignore below this line.


if __name__ == '__main__':
    run()
