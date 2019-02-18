# Title: DecIPAddress2BinIPAddress
# Created by: Samit Shaikh
# Created: 2019-02-18 14:01:23.209621
# Date of Last Revision: 2019-02-18 14:01:23.209650
# Purpose: To convert IPv4 Addresses with their subnet masks to binary from decimal.

# WORK IN PROGRESS THIS CODE PROBABLY MAY NOT WORK AND EVEN BE DANGEROUS!!!!

# Imports
def networkingdec2bin(address):


# code here


def run():
    print('Welcome to Decimal IPv4 Address with Subnet Mask to Binary program created by me, Samit Shaikh!'
          '    Dotted Decimal Notation'
          '-------------------------------')
    decip = input('IPv4 Address | ')
    print('-------------------------------')
    decsubnet = input(' Subnet Mask | ')
    print('-------------------------------'
          '         Converting...\n')
    binip = networkingdec2bin(decip)
    binsubnet = networkingdec2bin(binsubnet)
    if not binip[0]:
    # If binip is invalid then
    elif not binsubnet[0]:
    # if binsubnet is invalid then
    else:
        print('-------------------------------')
        print('IPv4 Address | ' + binip[1])
        print('-------------------------------')
        print(' Subnet Mask |')
        print('-------------------------------')


# Ignore below this line.


if __name__ == '__main__':
    run()
