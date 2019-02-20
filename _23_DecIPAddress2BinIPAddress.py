# Title: DecIPAddress2BinIPAddress
# Created by: Samit Shaikh
# Created: 2019-02-18 14:01:23.209621
# Date of Last Revision: 2019-02-18 14:01:23.209650
# Purpose: To convert IPv4 Addresses with their subnet masks to binary from decimal.

# Imports


def networkingdec2bin(address):
    if address.count('.') == 3 and address.count('..') == 0 and address.count('...') == 0:
        parts = address.split('.')
        newparts = ['', '', '', '']
        isvalid = True
        for i in range(len(parts)):
            if parts[i].isdigit():
                if -1 < int(parts[i]) < 256:
                    newparts[i] = format(int(str(bin(int(parts[i]))).replace('0b', '')), '08d')
                else:
                    newparts[i] = 'INVALID!'
                    isvalid = False
            else:
                newparts[i] = 'INVALID!'
                isvalid = False
        return [isvalid, '.'.join(newparts)]
    else:
        return [False, 'INVALID!']


def run():
    print('Welcome to Decimal IPv4 Address with Subnet Mask to Binary\nprogram created by me, Samit Shaikh!')
    print('\n              Dotted Decimal Notation              \n'
          '---------------------------------------------------')
    decip = input('IPv4 Address | ')
    print('---------------------------------------------------')
    decsubnet = input(' Subnet Mask | ')
    print('---------------------------------------------------')
    loop = True
    while loop:
        print('\n                  Converting...\n')
        binip = networkingdec2bin(str(decip))
        binsubnet = networkingdec2bin(str(decsubnet))
        restart = False
        print('              Dotted Binary Notation              \n'
              '---------------------------------------------------')
        print('IPv4 Address | ' + binip[1])
        if not binip[0]:
            decip = input('             | Not between 0 and 255 or does or\n'
                          '             | does not have 3 dots. To exit\n'
                          '             | just press enter you can exit after.\n'
                          '    Re-enter | ')
            restart = True
        print('---------------------------------------------------')
        print(' Subnet Mask | ' + binsubnet[1])
        if not binsubnet[0]:
            decsubnet = input('             | Not between 0 and 255 or does or\n'
                              '             | does not have 3 dots. To exit\n'
                              '             | just press enter you can exit after.\n'
                              '    Re-enter | ')
            restart = True
        print('---------------------------------------------------')
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
                print('Welcome to Decimal IPv4 Address with Subnet Mask to Binary program created by me, Samit Shaikh!')
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


# Ignore below this line.


if __name__ == '__main__':
    run()
