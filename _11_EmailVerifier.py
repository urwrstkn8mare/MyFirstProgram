# PRG11

# Rules to define an Email Address:
# From http://rumkin.com/software/email/rules.php
"""1 The email has a localpart on the left of an @, the domain on the right. Neither the localpart nor the domain may
be empty. 2 The localpart must be 64 characters or less. 3 The localpart can consist of labels separated by dots but
there can not be two successive dots, nor can it start or end with a dot. 3a    Labels must have at least one
character. 3b    Labels can only contain a-z, A-Z, 0-9, or any of !#$%&'*+-/=?^_`{|}~. 4 The domain can be bracketed,
unbracketed, or an IP address.. 5 Domain consists of labels separated by periods and less than 253 characters. No
domain can start with a period, end with a period, or have two successive periods. 5a    Labels consist of a-z, A-Z,
0-9, or one of !#$%&'*+-/=?^_`{|}~. 5b    Labels must be less than 63 characters. 5c    Labels must not start with a
hyphen, end with a hyphen, or contain two successive hyphens. 5d    The right-most label must be all alphabetic. """

# Imports all necessary modules for programs.
from email.utils import parseaddr
import os
import urllib.request
import file


def comments(email):
    newemail = email
    while True:
        if newemail.find('(') == -1:
            break
        else:
            if newemail.find(')') == -1:
                break
            else:
                a = newemail.split('(')
                a = '('.join(a[1:])
                b = a.split(')')
                comment = '(' + b[0] + ')'
                newemail = newemail.replace(comment, '')
    print('     LOG>>> Removed comments and now testing on <' + newemail + '>')
    return newemail


def strbool(inputvar):
    if inputvar:
        output = 'Valid'
    else:
        output = 'Invalid'
    return output


def log(functionreturn):
    # Log information returned by function run (the function is the rule in this case).
    print('     LOG>>> ' + functionreturn[0] + '() returned ' + strbool(functionreturn[1]) + '.')
    return functionreturn[1]


def testfunction(email):
    # Function to demonstrate how the rule should work.
    if email == email:
        pass
    else:
        pass
    return ['testfunction', True]


def checkat(email):
    # To check if there is an @.
    if email.find('@') == -1:
        # Returns False if @ is not found.
        returnvar = False
    else:
        # Runs following code if it does find @.
        # Makes a list variable, splitemail, which is assigned to the email split around an @.
        splitemail = email.split('@')
        # Makes a string variable, domain, which is assigned to the last string of the list variable, splitemail.
        domain = splitemail[-1]
        # Makes a string variable, localpart, with the third value returned by the function, atcheck().
        localpart = atcheck(email)[2]
        # Checks if variable, localpart, contains anything.
        if localpart == '':
            # Returns False if variable, localpart, contains nothing.
            returnvar = False
        else:
            # Runs following code if variable, localpart, contains something.
            # Checks if domain contains anything.
            if domain == '':
                # Returns False if variable, domain, contains nothing.
                returnvar = False
            else:
                # Runs following code if variable, domain, contains something.
                # Checks if variable, domain contains and period.
                if domain.find('.') == -1:
                    # Returns False if period was not found.
                    returnvar = False
                else:
                    # Runs following if period was found.
                    # Makes list variable, newsplitdomain, which is set to the domain split around periods.
                    newsplitdomain = domain.split('.')
                    # Checks if the first string in list variable, newsplitdomain, containes anything.
                    if newsplitdomain[0] == '':
                        # If the first string in list variable, newsplitdomain, contains nothing then return False.
                        returnvar = False
                        # Checks if the last string in list variable, newsplitdomain, contains anything.
                    elif newsplitdomain[-1] == '':
                        # Returns False if the last string in list variable, newsplitdomain, contains nothing.
                        returnvar = False
                    else:
                        # Returns True if both the first and last string in list variable, newsplitdomain, contains
                        # something.
                        returnvar = True
    return ['checkat', returnvar]


def doubleat(email):
    at = '@'
    i = 0
    returnvar = True
    while True:
        if email.find(at) == -1:
            break
        else:
            i += 1
            if i > 1:
                returnvar = returnvar and False
            else:
                returnvar = returnvar and True
            at = at + '@'
    return ['doubleat', returnvar]


def localpartdotcheck(email):
    # To check rule 3.
    # Makes string varaiable, localpart, the third variable returned by atcheck().
    localpart = atcheck(email)[2]
    # Makes stringvariable, localpartsplit, variable, localpart, split around the period.
    localpartsplit = localpart.split('.')
    # Makes integer variable, ii, 0.
    ii = 0
    # Returns True
    returnvar = True
    # Loops until integer variable, ii, is the same or bigger than the number of strings in list variable,
    # localpartsplit.
    while ii < len(localpartsplit):
        # Checks if the variable, ii, string of variable, localpartsplit, contains anything.
        if localpartsplit[ii] == '':
            # If the variable, ii, string of variable, localpartsplit, contains nothing it returns the previous
            # return and False and breaks the loop.
            returnvar = returnvar and False
            break
        else:
            # If the variable, ii, string of variable, localpartsplit, contains something it returns the previous
            # return and True and adds 1 to variable, ii.
            returnvar = returnvar and True
            ii += 1
    return ['localpartdotcheck', returnvar]


def atcheck(email):
    # To allow other functions to find the localpart even if there are two @'s (was supposed to be mainly used by the
    #  the quotation checker.) Makes integer varibale, i, 0.
    i = 0
    # Makes integer varibale, atnumber, 0.
    atnumber = 0
    # Loops while varible, i, is smaller than the number of characters in variable, email.
    while i < len(email):
        # Checks if variable, i, of email contains @.
        if email[i] == '@':
            # If True then add 1 to varibale, atnumber, and varibale, i.
            atnumber += 1
            i += 1
        else:
            # If False then add 1 to variable, i.
            atnumber += 0
            i += 1
    # Makes integer variable, ats, the variable, atnumber.
    ats = atnumber
    # Makes list variable, localpart, the argument, email, split around @.
    localpart = email.split('@')
    # Check if variable, ats, is bigger than 1.
    if ats > 1:
        # If variable, ats, is bigger than 1, than run following.
        # Make string varible, newlocalpart, the first string in the list variable, localpart.
        newlocalpart = localpart[0]
        # Make integer variable, i, 1.
        i = 1
        # Loop while variable, i, is smaller than variable, ats, minus 1.
        while i < ats - 1:
            # Make variable, newlocalpart, newlocalpart joined with the variable, i, string of localpart.
            newlocalpart = newlocalpart + localpart[i]
            i += 1
    else:
        newlocalpart = localpart[0]
    localpart = newlocalpart
    return ['atcheck', True, localpart]


def pythonparser(email):
    if parseaddr(email) == ['', '']:
        returnvar = False
    else:
        returnvar = True
    return ['pythonparser', returnvar]


def alphabet(email):
    returnvar = True
    localpart = atcheck(email)[2]
    domain = email.split('@')[-1]
    alphabetthird = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#$%&' + '\'*+-/=?^_`{|}~.'
    i = 0
    while i < len(alphabetthird):
        localpart = localpart.replace(alphabetthird[i], '')
        domain = domain.replace(alphabetthird[i], '')
        i += 1
    if localpart == '' and domain == '':
        pass
    else:
        returnvar = False
    return ['alphabet', returnvar]


def checklocalpartlength(email):
    returnvar = True
    localpart = atcheck(email)[2]
    if 0 < len(localpart) < 65:
        returnvar = returnvar and True
    else:
        returnvar = returnvar and False
    return ['checklocalpart', returnvar]


def checkdomain(email):
    returnvar = True
    domain = email.split('@')[-1]
    if 5 < len(domain) < 65:
        pass
    else:
        returnvar = False
    firstdot = domain.find('.')
    domain = domain[:firstdot]
    domainsplit = domain.split('-')
    ii = 0
    while ii < len(domainsplit):
        if domainsplit[ii] == '':
            returnvar = returnvar and False
            break
        else:
            returnvar = returnvar and True
            ii += 1
    return ['checkdomain', returnvar]


def checktopleveldomain(email):
    domain = email.split('@')[-1]
    toplevel = domain.split('.')[1:]
    i = 0
    tld = file.read('tlds-alpha-by-domain.txt', 0)
    tld = tld[1:]
    tld.append('WA')
    returnvar = True
    while i < len(toplevel):
        ii = 0
        testtld = 0
        while ii < len(tld):
            if toplevel[i] == tld[ii].lower():
                testtld += 1
            else:
                testtld += 0
            ii += 1
        if testtld == 1:
            returnvar = returnvar and True
        else:
            returnvar = returnvar and False
        i += 1
    return ['checktopleveldomain', returnvar]


def checkemailbulk():
    while True:
        print('')
        print('Please input the path of the ".txt" file containing email addresses on each file.')
        filename2 = str(input('     -> '))
        if filename2[-4:] == '.txt':
            break
        else:
            print('Incorrect file extension, must be ".txt". Try Again...')
    filename = filename2
    fn = filename2.split('/')[-1]
    filename2 = filename2.replace(fn, '')
    resultsfilename = filename2 + "resultsfor" + fn
    f = file.openforwrite(resultsfilename)
    print(
        'Please note that if you already have a file named "' + resultsfilename + '", it will be erased and replaced.')
    input('Enter to continue. Quit if you want.')
    print('')
    print('Opening -> ' + filename)
    print('')
    fileinfo = file.read(filename, 0)
    numberofemails = len(fileinfo)
    print('Found ' + str(numberofemails) + ' items   -> ')
    print('')
    i = 0
    while i < len(fileinfo):
        emailnumber = i + 1
        print(' ' + str(emailnumber) + ' - ' + fileinfo[i])
        i += 1
    print('')
    print('     <- ')
    print('')
    print('Running tests...')
    print('')
    print('Starting Process...')
    emailcount = 0
    file.write(f, 'Reslts for email validation:')
    print('')
    fileinforesults = []
    while emailcount < numberofemails:
        print(' Tests for <' + fileinfo[emailcount] + '> : ')
        fileinforesults.append(True)
        email = comments(fileinfo[emailcount])
        test = 0
        """This is where the functions (rules) are laid out (each returns Valid or Invalid): """
        tests = {0: testfunction,
                 1: pythonparser,
                 2: checkat,
                 3: localpartdotcheck,
                 4: checklocalpartlength,
                 5: checkdomain,
                 6: alphabet,
                 7: checktopleveldomain,
                 }
        while test < len(tests):
            fileinforesults[emailcount] = fileinforesults[emailcount] and log(tests[test](email.lower()))
            test += 1
            if not fileinforesults[emailcount]:
                break
            else:
                pass
        """End"""
        print(strbool(fileinforesults[emailcount]) + ': <' + fileinfo[emailcount] + '>')
        file.write(f, str(fileinfo[emailcount]) + " [" + strbool(fileinforesults[emailcount]) + "]")
        emailcount += 1
        print('')
    file.closeafterwrite(f)
    print(
        'Email Validation Finished. New file created (' + resultsfilename + ') with results inside. Program ending.')
    t = 0
    x = 0
    y = 0
    while t < len(fileinforesults):
        if fileinforesults[t]:
            x += 1
        else:
            y += 1
        t += 1
    total = x + y
    percentx = (x / total) * 100
    percenty = (y / total) * 100
    print('Number of valid: ' + str(x) + '/' + str(total) + ' OR ' + str(percentx) + '%')
    print('Number of invalid: ' + str(y) + '/' + str(total) + ' OR ' + str(percenty) + '%')
    os.remove('tlds-alpha-by-domain.txt')
    print('')
    return


def checkmailindividual():
    print('Please input the email address. ')
    fileinfo = [input('     -> ')]
    numberofemails = len(fileinfo)
    fileinfo[0] = fileinfo[0].rstrip()
    print('')
    print('Running tests...')
    print('')
    print('Starting Process...')
    emailcount = 0
    print('')
    fileinforesults = []
    while emailcount < numberofemails:
        print(' Tests for <' + fileinfo[emailcount] + '> : ')
        email = comments(fileinfo[emailcount])
        fileinforesults.append(True)
        test = 0
        """This is where the functions (rules) are laid out (each returns Valid or Invalid): """
        tests = {0: testfunction,
                 1: pythonparser,
                 2: checkat,
                 3: doubleat,
                 4: localpartdotcheck,
                 5: checklocalpartlength,
                 6: checkdomain,
                 7: alphabet,
                 8: checktopleveldomain,
                 }
        while test < len(tests):
            fileinforesults[emailcount] = fileinforesults[emailcount] and log(tests[test](email.lower()))
            test += 1
            if not fileinforesults[emailcount]:
                break
            else:
                pass
        """End"""
        print(strbool(fileinforesults[emailcount]) + ': <' + fileinfo[emailcount] + '>')
        emailcount += 1
        print('')
    os.remove('tlds-alpha-by-domain.txt')
    return


def run():
    while True:
        print('Downloading http://data.iana.org/TLD/tlds-alpha-by-domain.txt ')
        url = 'http://data.iana.org/TLD/tlds-alpha-by-domain.txt'
        urllib.request.urlretrieve(url, 'tlds-alpha-by-domain.txt')
        print('File downloaded successfully.')
        print('')
        print('Do you want to check emails in bulk or individually through console? (1/2)')
        choice = str(input('    -> '))
        print('')
        if choice.lower() == 'bulk' or choice.lower() == '1':
            checkemailbulk()
            print('Restart? (y/n)')
            choice2 = str(input('    -> '))
            if choice2.lower() == 'y':
                pass
            else:
                print('Exiting...')
                break
        elif choice.lower() == 'console' or choice.lower() == '2':
            checkmailindividual()
            print('Restart? (y/n)')
            choice2 = str(input('    -> '))
            if choice2.lower() == 'y':
                pass
            else:
                print('Exiting...')
                break
        else:
            print('Invalid Response, try again...')
        return


if __name__ == '__main__':
    run()

os.remove('file.py')
