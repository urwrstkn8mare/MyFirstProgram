import urllib.request
import os

print('Downloading http://urwrstkn8mare.000webhostapp.com/samit/projects/py/file.py ...')
url = 'http://urwrstkn8mare.000webhostapp.com/samit/projects/py/file.py'
urllib.request.urlretrieve(url, 'file.py')
import file


def findthing(email, string):
    check = email.find(string)
    if check == -1:
        returnvar = True
    else:
        returnvar = False
    return returnvar


def cleanup(textfile):
    print('')
    print('Reading ' + textfile + '...')
    txt = file.read(textfile, 0)
    i = 0
    print('Found ' + str(len(txt)) + ' items:')
    while i < len(txt):
        print(txt[i])
        i += 1
    i = 0
    print('')
    print('Finding problems...')
    print('')
    newnewtxt = ['']
    while i < len(txt):
        test = findthing(txt[i], ':')
        test = test and findthing(txt[i], '[')
        test = test and findthing(txt[i], ']')
        test = test and findthing(txt[i], '"')
        if test:
            print('No problem found with ' + txt[i])
            newnewtxt.append(txt[i])
        elif not test:
            print('Problem found with ' + txt[i] + '. Cleaning...')
        i += 1
    del newnewtxt[0]
    print('Checking complete.')
    print('')
    print('Opening for write...')
    newtxt = file.openforwrite(textfile)
    i = 0
    print('')
    print('New file being created:')
    print('')
    while i < len(newnewtxt):
        string = newnewtxt[i]
        string = string.replace('invalid', '')
        string = string.replace('valid', '')
        string = string.replace('[True]', '')
        string = string.replace('[False]', '')
        string = string.replace('[Valid]', '')
        string = string.replace('[Invalid]', '')
        string = string.rstrip()
        print(string)
        file.write(newtxt, string)
        i += 1
    print('')
    print('Done')
    file.closeafterwrite(newtxt)
    return


def run():
    while True:
        cleanup(input('Please input the text file (with ending of .txt): '))
        print('')
        restart = input('Restart? (y/n)')
        if restart.lower() == 'y':
            pass
        else:
            break


if __name__ == '__main__':
    run()

os.remove('file.py')
