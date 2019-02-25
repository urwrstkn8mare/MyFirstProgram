# Title: DecIPAddress2BinIPAddress
# Created by: Samit Shaikh
# Created: 2019-02-18 14:01:23.209621
# Date of Last Revision: 2019-02-25
# Purpose: To convert IPv4 Addresses with their subnet masks to binary from decimal.
# This program relies on _15_BinaryConverterAndStuff.py

# Imports the dec2bin() funtion from _15_BinaryConverterAndStuff.py which is used
# to convert decimals to binary numbers.
from _15_BinaryConverterAndStuff import dec2bin


# This function: ValidateIP4() accepts a string which is supposed to be the IP address and checks if it a valid
# IPO address. If it is valid then it will convert it to a binary ip address.
def ValidateIP4(address):
    # This is check 1 of the tests the IP Address must pass to be accepted. Check 1 checks if the IP Address
    # has 3 decimal points. However, there must be something between them. To check this it checks for any
    # double or triple decimal points that could be there.
    if address.count('.') == 3 and address.count('..') == 0 and address.count('...') == 0:
        # Ounce the address passes check 1 it is split between the decimal points and each part is put into an array.
        # The array should have 4 items.
        parts = address.split('.')
        # A array variable call newparts is created with four items with empty strings for use later.
        newparts = ['', '', '', '']
        # Another variable, this time boolean, isvalid is created with the value of True. This is if the IP address
        # is invalid then it can be known by the returned value of this function.
        isvalid = True
        # Then it carry's out two checks on each part of the address (or each item in the array) with a loop.
        for i in range(len(parts)):
            # Check 2 is checking if the part is actually an integer.
            if parts[i].isdigit():
                # If the part passes check 2 then it proceeds with another check. Check 3 is checking if the part
                # is between 0 and 255 inclusive because that is the requirments of a valid IP Address.
                if -1 < int(parts[i]) < 256:
                    # If the part passes check 3 than it is converted to a binary format making sure there is
                    # always 8 digits in the string. Then it is added to the corresponding item on a new newparts
                    # array. Nothing happens to isvalid and it stays whatever value it was previously.
                    newparts[i] = format(
                        int(str(dec2bin(int(parts[i])))), '08d')
                else:
                    # If the part fails check 3 than it puts the a string with 'INVALID!' in the corresponding item
                    # in the newparts array and isvalid is set to false.
                    newparts[i] = 'INVALID!'
                    isvalid = False
            else:
                # If the part fails check 2 the same thing that happens if the part fails check 3, happens.
                newparts[i] = 'INVALID!'
                isvalid = False
        # After all the checks and coversions an array consisting of two values is outputted. The first value is
        # the boolean variable, isvalid and the second is the array, newparts, joined together with decimal
        # points as a string. This string is the new dotted binary IP address.
        return [isvalid, '.'.join(newparts)]
    else:
        # If the IP Address fails check 1 then an array consisting of two values is ouputted. The first value is
        # False indicating that the IP Address is invalid and the second is a string saying 'INVALID!'. This is
        # there because there is nothing else to put there because the IP Address was invalid.
        return [False, 'INVALID!']


def run():
    # An introduction to the program. :)
    print('Welcome to Decimal IPv4 Address with Subnet Mask to Binary\nprogram created by me, Samit Shaikh!')
    # This sets out the table like structure where the user inputs the two IP addresses.
    print('\n              Dotted Decimal Notation              \n'
          '---------------------------------------------------')
    decip = input('IPv4 Address | ')
    print('---------------------------------------------------')
    decsubnet = input(' Subnet Mask | ')
    print('---------------------------------------------------')
    # This makes the default value of the new variable loop, True.
    loop = True
    # The rest of the code runs as long as the variable, loop, is True.
    while loop:
        print('\n                  Converting...\n')
        # The two IP addresses are converted and stored in the new variables: binip & binsubnet.
        binip = ValidateIP4(str(decip))
        binsubnet = ValidateIP4(str(decsubnet))
        # The new boolean variable, restart, is set to False.
        restart = False
        # The following is a similiar table to above but with the binary IP address equivelents. If there is an
        # invalid address, the user knows and is given the chance to re-enter another IP address which will be
        # converted later (more on that later).
        print('              Dotted Binary Notation              \n'
              '---------------------------------------------------')
        print('IPv4 Address | ' + binip[1])
        if not binip[0]:
            decip = input('             | Not an integer between 0 and 255 or\n'
                          '             | does not have 3 dots. To exit\n'
                          '             | just press enter you can exit after.\n'
                          '    Re-enter | ')
            restart = True
        print('---------------------------------------------------')
        print(' Subnet Mask | ' + binsubnet[1])
        if not binsubnet[0]:
            decsubnet = input('             | Not an integer between 0 and 255 or\n'
                              '             | does not have 3 dots. To exit\n'
                              '             | just press enter you can exit after.\n'
                              '    Re-enter | ')
            restart = True
        print('---------------------------------------------------')
        # If the one of the IP addresses were invalid and had to be re-entered then restart would have been set to
        # True. If this was the case then the user will be given the chance to convert the re-entered IP addresses
        # or he/she can exit the program. Other wise the program will ask the user if he/she wants to re-run the
        # program (restart). If yes it will, if not then it will not. Kinda self-explanatory. It uses the loop
        # variable to stop the program from re-running or to let it re-run.
        if restart:
            print('\nAt least one of the IP Address was invalid so you\nmust restart the converter with your new '
                  'address.')
            if input('Restart or Exit? (y/n) -> ').lower() == 'y':
                loop = True
                print('\nRestarting...')
            else:
                loop = False
                print('\nThe program will end now.')
        else:
            if input('\nRestart? (y/n) -> ').lower() == 'y':
                print('Restarting...\n')
                print(
                    'Welcome to Decimal IPv4 Address with Subnet Mask to Binary program created by me, Samit Shaikh!')
                print('\n    Dotted Decimal Notation    \n'
                      '---------------------------------------------------')
                decip = input('IPv4 Address | ')
                print('---------------------------------------------------')
                decsubnet = input(' Subnet Mask | ')
                print('---------------------------------------------------')
                loop = True
            else:
                loop = False
                print('\nGoodbye!')


# Ignore below this line (it is just so the UI elements don't show up when another program wants to use some of
# the functions). The UI code is in the function run so programs like my startup program I made for fun can run
# it if it wants.
if __name__ == '__main__':
    run()
