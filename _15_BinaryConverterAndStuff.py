# Yr8CS1_Samit Shaikh_20180809
# Binary Converter

import os

logr = input('LOG (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                               'uh-huh']  # If userinput is in the list then variable logr is True
print()  # Print new line


# To use command system:
# command: <command>-<value>,<value2>
# eg. command: largest-5,4,3
# eg. command: dec2bin-540
# eg. command: asc2dec-!
# (find function names in code)


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


def dec2bin(number):  # defines function as dec2bin
    try:
        number = int(number)  # turns variable number into integer
        log(number, logr)  # logs variable number
        if str(number).find('-') > -1:  # checks if their is a '-' in number
            number = str(number).replace('-', '')  # if returned true than variable number has the '-' removed
            number = int(number)  # make number variable back into integer
            negative = True  # set boolean variable negative to true.
        else:
            negative = False  # if returned false, boolean variable negative is set false
        log(number, logr)  # log variable number
        log(negative, logr)  # log variable negative
        if number == 0:  # checks if variable number is 0
            binumber = '0'  # if returned true, sets string variable binumber to '0'
            log(binumber, logr)  # logs variable binumber
        else:
            binumber = ''  # if returned false, sets string variable binumber to empty string
            log(binumber, logr)  # logs variable binumber
            while number > 0:  # loops if variable number is less than 0
                binumber = str(
                    number % 2) + binumber  # sets variable binumber to the remainder of variable number divided by 2 added to the left of variable binumber as a string
                number = number // 2  # sets variable number to variable number divided by 2 without remainders or in decimal form
                log(binumber, logr)  # logs variable binumber
                log(number, logr)  # logs variable number
        if negative:  # checks if variable negative is true
            binumber = '-' + binumber  # if returned true, variable binumber has '-' added to the left of itself
        else:
            pass  # if returned false, do nothing
        log(binumber, logr)  # logs binumber
        binumber = int(binumber)
    except ValueError:
        print('! Must input number !')
        binumber = 'error'
    return binumber  # returns binumber as an integer


def bin2dec(number):  # defines function as bin2dec
    bbinary = str(number)  # sets bbinary to variable number as string
    log(bbinary, logr)  # logs variable bbinary
    ddecimal = 0  # sets ddecimal to 0
    log(ddecimal, logr)  # logs variable ddecimal
    i = 0  # sets i to 0
    while i < len(bbinary):  # loops while i is less than the number of characters in variable bbinary
        log(0 - (i + 1), logr)  # logs the output of variable i add 1 subtracted from 0
        log(i, logr)  # logs variable i
        mathh = ((2 ** i) * int(bbinary[0 - (i + 1)]))
        log(mathh, logr)  # log variable mathh
        ddecimal = ddecimal + mathh  # sets variable ddecimal to itself added to varibale mathh
        log(ddecimal, logr)  # log variable ddecimal
        i += 1  # sets variable i to 1 added to itself
    return ddecimal  # returns variable ddecimal


def dec2asc(number):  # define function dec2ascii
    dec = int(number) - 32  # sets variable dec to variable number subtract 32 as an integer
    asciiTable = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    # sets variable asciiTable to printable range of ascii characters in a string with placeholders on it's right to align the position of each character to its corresponding decimal value.
    if 31 < dec + 32 < 127:
        pass  # checks if variable dec plus 32 is between 31 and 127
    else:
        print('!ERROR! Input not within printable range.')  # if returned false, print an error with reason
        exit()  # exit program
    return asciiTable[
        dec]  # return the character in variable asciiTable which position is the value held in variable dec.


def bin2asc(number):  # define function bin2ascii
    return dec2asc(bin2dec(
        number))  # return the output of function dec2ascii which argument is the output of function bin2dec. Function bin2dec's argument is variable number


def asc2dec(letter):  # define function ascii2dec
    if len(str(letter)) == 1:
        pass
    else:
        print('!ERROR! Input more than one letter (or less)')  # if returned false, print error
        exit()  # exit program
    asciiTable = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    # sets variable asciiTable to printable range of ascii characters in a string with placeholders on it's right to align the position of each character to its corresponding decimal value.
    return asciiTable.find(str(letter)) + 32


def asc2bin(letter):  # defines function ascii2bin
    return dec2bin(asc2dec(
        letter))  # return the output of function dec2bin which argument is the output of function ascii2dec. Function ascii2dec's argument is variable letter


def largest(a, b, c):  # defines function largest
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b:  # checks if variable a is bigger than variable b
        one = a  # if returned true, variable one is given variable a
        two = b  # variable two is given variable b
    else:
        one = b  # if returned false, variable one is given variable b
        two = a  # variable two is given variable a
    if two < c < one:  # checks if variable two is bigger than c and variable c is bigger than variable one
        three = two  # if returned true, variable three is given variable two
        two = c  # variable two is given variable c
    elif two < one < c:  # else, checks if variable two is bigger than variable one and variable c is bigger than variable c
        three = two  # variable three is given variable two
        two = one  # variable two is given variable one
        one = c  # variable one is given variable c
    else:  # else
        three = c  # else, variable three is given variable c
    return [int(one), int(two), int(three)]  # returnes a list containing variables one, two and three


def smallest(a, b, c):  # defines function smallest
    lrgfnc = largest(a, b,
                     c)  # variable lrgfnc is given the ouput of function largest which arguments are variables a, b and c
    return [lrgfnc[2], lrgfnc[1], lrgfnc[
        0]]  # returns list containing the last of list variable lrgfnc, the second of variable lrgfnc and the first of variable lrgfnc


def writefileval(textfilename, mystring):
    f = open(str(textfilename), 'w+')
    f.write(str(mystring) + '\n')
    f.close()
    return


def readfileval(textfilename):
    global content
    try:
        with open(str(textfilename)) as fr:
            content = fr.readlines()
            """to remove whitespace characters like `\n` at the end of each line"""
            content = [xx.strip() for xx in content]
    except FileNotFoundError:
        error = 'ERROR! The file you gave was not found or there was a problem with the program. (the file must be in the same directory as this program.)'
        print('\n' + error)
        input()
        exit()
    return content


def restart():
    restartt: str = input('\nRestart? (y/n) \n')  # sets variable restart to user input
    if restartt.lower() == 'y':  # if variable restart, with all characters in lowercase, is 'y'
        return False
    else:
        return True


def run():
    global cmd, value
    while True:  # loops forever unless broken
        try:
            command = str(input('command: '))  # sets variable command to user input as string.
            log(command, logr)  # logs variable command
            command = command.split('-', 1)  # splits variable command between the first '-'
            log(command, logr)  # logs variable command
            value = command[1]  # sets variable value to the second string in list variable command
            cmd = command[0]  # sets variable cmd to the first string in list variable command
            log(value, logr)  # logs variable value
            log(cmd, logr)  # logs variable value
            value = value.split(',')  # splits variable value between ','
            log(value, logr)  # logs variable value
        except IndexError:
            print('!ERROR! Command not split from value by \'-\'')
            if restart():
                break
        try:  # tries following code
            if cmd == 'dec2bin':  # if variable cmd is 'dec2bin'
                print(dec2bin(value[
                                  0]))  # then prints output of function dec2bin which argument is the first of list variable value as an integer
            elif cmd == 'bin2dec':  # if above is false then if variable cmd is 'bin2dec'
                print(bin2dec(value[
                                  0]))  # then prints output of function bin2dec which argument is the first of list variable value as an integer
            elif cmd == 'dec2asc':  # if above is false then if variable cmd is 'dec2ascii'
                print(dec2asc(value[
                                  0]))  # then prints output of function dec2ascii which argument is the first of list variable value as an integer
            elif cmd == 'bin2asc':  # if above is false then if variable cmd is 'bin2ascii'
                print(bin2asc(value[
                                  0]))  # then prints output of function bin2ascii which argument is the first of list variable value
            elif cmd == 'asc2dec':  # if above is false then if variable cmd is 'ascii2dec'
                print(asc2dec(value[
                                  0]))  # then prints output of function ascii2dec which argument is the first of list variable value
            elif cmd == 'asc2bin':  # if above is false then if variable cmd is 'ascii2bin'
                print(asc2bin(value[
                                  0]))  # then prints output of function ascii2bin which argument is the first of list variable value
            elif cmd == 'largest':
                print(largest(value[0], value[1], value[2]))
            elif cmd == 'smallest':
                print(smallest(value[0], value[1], value[2]))
            elif cmd == 'writefileval':
                print(writefileval(value[0], value[1]))
            elif cmd == 'readfileval':
                print(readfileval(value[0]))
            elif cmd == 'log':  # if above is false then if variable cmd is 'log'
                print(log(value[0], logr))  # logs the first of list variable value
            else:
                print('!ERROR! Command not found.')  # else, print error
                if restart():
                    break
        except IndexError:  # if their is an IndexError
            print('!ERROR! Too many or not enough values inputted.')  # then print error
            if restart():
                break
        if restart():
            break


if __name__ == '__main__':
    run()
