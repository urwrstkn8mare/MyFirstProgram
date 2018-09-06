logr = input('LOG (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                               'uh-huh']  # If userinput is in the list then variable logr is True
print()  # Print new line


def log(text, validator, **opt):  # Define function log with parameters: name, text and validator
    name = '' # Store an empty string in variable name.
    if 'name' in opt: # If there is an optional parameter named 'name' then...
        name = opt['name'] # ...store 'name' of the optional parameters in name.
    if validator:  # If variable validator is True then...
        print('LOG>>> ' + str(text) + ' <<< ' + str(name))  # ... print 'LOG>>>', variable text, '<<<' then variable nameself.
    if 'wait' in opt: # If there is an optional parameter named 'wait' then...
        if opt['wait']: # ...if 'wait' of opt is True then...
            input('LOG>>> Enter to continue >>>') # ...wait for user to enter to continue.

def error(err, string):  # Define function error with parameters: err and string
    print(err + ' ' + string)  # Print variables err and string with a space in between.
    return err  # Return variable err.


def exist(filename): # Define function exist with parameter filename/
    try: # Tries...
        opener = open(str(filename))  # ...to open file which name is stored in variable filename.
    except FileNotFoundError: # If there is an error, FileNotFoundError, then
        return False  # ...return False.
    return True  # If there is no error, return True.


def read_csv(filename, header): # Define function read_csv with parameters: filename and header.
    while True:  # Infinitely loop the following until broken.
        if filename.endswith('.csv'): # If variable filename's string ends with '.csv' then...
            try:
                with open(str(filename)) as fr: # ...try to open file which name is stored in variable filename as fr.
                    content = fr.readlines() # Store list containing each line in the opened file, fr, as a list item.
                    content = [xx.strip() for xx in content] # Removes whitespace (eg. ' ', '\n') from each line in list variable content.
            except FileNotFoundError: # If there is an error, FileNotFoundError, then...
                return error('!ERROR_02!',
                             'The file you gave was not found or there was a problem with the program. (the file must '
                             'be in the same directory as this program.)')  # return a custom error.
            for i in range(len(content)): # While variable i is in the range of the number of list items in content...
                if not ',' in content[i]: # If there is not a ',' in variable i of content...
                    return error('!ERROR_03!', 'Not formatted correctly according to CSV format.') # ..return a custom error.
            log('VERIFIED', logr) # Log 'VERIFIED' if logr is True.
            pp = [] # Store an empty list in variable pp.
            log('LOOP x', logr) # Log 'LOOP X' if logr is true.
            for x in range(len(content)): # While variable x is in the range of the number of list items in content...
                xx = content[x].split(',') # ...split x of content around the commas and store the list output in variable xx.
                b = [] # Store an empty list in variable b.
                log('LOOP c', logr) # Log 'LOOP C' if logr is True.
                for c in range(len(xx)): # While variable c is in the range of the number of items in list variable xx...
                    log('LOOP y', logr) # ...log 'LOOP Y' if logr is True.
                    for y in range(len(xx)): # While variable y is in the range of the number of items in the list variable xx...
                        z = ','.join(xx[c:y + 1]) # ...join variable c to variable y plus 1 of list variable xx with commas and store it in variable z.
                        z = z.strip() # Remove whitespace (eg. ' ', '\n') from variable z.
                        log(z, logr, name='z')  # Log variable z if logr is True and with the name: 'z'.
                        log(str(z.startswith('\"')), logr, name='z.startswith(\'\"\')') # Log True if z starts with '"' if logr is true and with the name: 'z.startswith('"')'.
                        log(str(z.endswith('\"')), logr, name='z.endswith(\'\"\')') # Log True if z ends with '"' if logr is true and with the name: 'z.endswith('"')'.
                        if z.startswith('\"') and z.endswith('\"'): # If z starts with and ends with '""' then...
                            log(str([c, y + 1]), logr, name='[c, y + 1]') # ...log list containing c and y plus 1 if logr is True and with the name: '[c, y + 1]'.
                            b.append([c, y + 1]) # Append list containing c and y plus 1 to list variable b.
                b.append([-1, -1]) # Append list containing negative 1 and negative 1 to list variabel b.
                log(str(b), logr, name='b') # Log variable b if logr is True with the name: 'b'.
                p = [] # Store empty list in variable p.
                m = 0 # Store zero in variable m.
                u = 0 # Store zero in variable u.
                log(len(xx), logr, name='len(xx)') # Log the number of items in xx if logr is True with the name: 'len(xx)'.
                log('LOOP U', logr) # Log 'LOOP U' if logr is True.
                while u < len(xx): # While u is under the number of items in xx...
                    if u == b[m][0]: # ...,if u is the same as 0 of m of b then...
                        o = ','.join(xx[u:b[m][1]]) # ...join u to 1 of m of b of with commas and then store it in variable o.
                        log(o, logr, name='o (True)') # Log variable o if logr is True with the name: 'o (True)'.
                        u = b[m][1] # Store 1 of m of b in variable u.
                        log(u, logr, name='u (True)') # Log variable u if logr is True with the name: 'u (True)'.
                    else: # Else...
                        o = xx[u] # ...store u of xx in o.
                        log(o, logr, name='o (False)') # Log variable o if logr is True with the name: 'o (False)'.
                        u += 1
                        log(u, logr, name='u (False)') # Log variable u if logr is True with the name: 'u (False)'.
                    p.append(o.strip()) # Append o with whitespace removed to p.
                log(p, logr, name='pp')
                pp.append(p)
                log(pp, logr, name='pp')
            old = len(pp[0])
            log('LOOP H', logr)
            for h in range(len(pp)):
                new = len(pp[h])
                log(old, logr, name='old')
                log(new, logr, name='new')
                if old == new:
                    old = new
                else:
                    return error('!ERROR_04!', 'Not formatted correctly according to CSV format.')
            log(pp, logr, name='pp')
        else:
            return error('!ERROR_01!', 'The file does not have a .csv extension.')
        keys = []
        csvfile = []
        log('LOOP G', logr)
        for g in range(len(pp[0])):
            if header:
                keys.append(pp[0][g])
            else:
                keys.append(g)
        log(keys, logr, name='keys')
        log(header, logr, name='header')
        if header:
            q = 1
        else:
            q = 0
        log('LOOP Q', logr)
        while q < len(pp):
            b = {}
            for j in range(len(pp[q])):
                b[keys[j]] = pp[q][j]
            csvfile.append(b)
            q += 1
        log(csvfile, logr, name='csvfile')
        return csvfile


def find_csv_record(filename, key_value, **key):
    # there must be header and header must have a key field to use
    csvfile = read_csv(filename, True)
    if 'key' in key:
        keyy = key['key']
    else:
        keyy = 'key'
    for l in range(len(csvfile)):
        try:
            if csvfile[l][keyy] == key_value:
                return csvfile[l]
        except IndexError:
            return error(
                '!ERROR! CSV not formatted correctly to be used by this program.\nThere must be header and header '
                'must have a key field to use.')


def update_csv_record(filename, header, row, field, new_value):
    csvfile = read_csv(filename, header)
    try:
        csvfile[row][field] = new_value
    except IndexError:
        return error('!ERROR! Row and field are not found in file.')
    newfile = [', '.join(csvfile[0])]
    for l in range(len(csvfile)):
        ll = ','.join(csvfile[l])
        ll = ll.split(',')
        pp = []
        for g in range(len(ll)):
            pp.append(csvfile[l][ll[g]])
        newfile.append(', '.join(pp))
    f = open(filename, "w")
    writeto = ''
    for h in range(len(newfile)):
        writeto = writeto + newfile[h] + '\n'
    f.write(str(writeto))
    f.close()


def append_csv_record(filename, listt):
    if isinstance(listt, list):  # checks if listt is a list
        csvfile = read_csv(filename, False)  # reads filename with no headers and outputs into csvfile
        if len(listt) == len(csvfile[
                                 0]):  # checks if the number of items in listt is the same as the number of items in 0 of csvfile.
            with open(filename, 'a') as f:  # opens filename
                tmp = []
                for n in range(len(listt)):
                    tmp.append(str(listt[n]))
                f.write(', '.join(tmp) + '\n')
                f.close()
        else:  # else returns error
            return error(
                '!ERROR! CSV file will not be formatted correctly with this new row. (The number of fields in input '
                'is not the same as file inputted)')
    else:  # else returns error
        return error('!ERROR! Parameter list is not a list. (it should be)')


def write_csv_record(filename, inside):
    with open(filename, 'w') as f:  # opens filename with write permissions
        try:  # tries the following
            old = len(inside[0])  # make variable old the number of fields in inside[0]
            for d in range(len(inside)):  # loops while number d is in the number of items in inside.
                if isinstance(inside[d], list):  # checks if d of inside is a list
                    new = len(inside[d])  # makes new the number of items in d of inside
                    if old == new:  # checks if old is the same as new
                        tmp = []  # creates tmp list
                        for n in range(len(inside[d])):  # loops while n is in the number of items in d of inside
                            tmp.append(str(inside[d][n]))  # appends string form of n of d of inside
                        f.write(', '.join(
                            tmp) + '\n')  # joins together items in tmp with comma and writes it to the file. Adds a new line after.
                    else:  # else returns error
                        return error(
                            '!ERROR! Lines do not have same number of fields. (The file may be incomplete or corrupted.)')
                else:  # else returns error
                    return error(
                        '!ERROR! Parameters other than filename should be lists. (The file may be incomplete or corrupted.)')
        except IndexError:  # if there is an index error closes file and returns error
            f.close()
            return error('!ERROR! Parameters were incorrectly inputted. (The file may be incomplete or corrupted.)')
        f.close()  # closes file


def insert_csv_record(filename, listt, index):
    data = read_csv(filename, False)  # reads file and outputs into data
    listdata = []  # creates empty list, listdata
    for i in range(len(data)):  # while i is in the number of items in data
        tmpitem = []  # creates emptyl list, tmpitem
        for n in range(len(data[i])):  # while n is in the number of items in i of data
            tmpitem.append(data[i][n])  # appends to tmpitem n of i of data
        listdata.append(tmpitem)  # appends tmpitem to listdata
    listdata.insert(int(index), listt)  # inserts listt at index into listdata
    for b in range(len(listdata)):  # while b is in the number of items in listdata
        if not len(listdata[b]) == len(listdata[0 - (len(listdata) - b)]):  # checks if the number of items in b of
            # listdata is not equal to the number of items in (0 - len(listdata) - b) of listdata). Also returns error after
            return error('!ERROR_INCORRECT!', 'New line does not have the same amount of fields as other lines.')
    write_csv_record(filename, listdata)  # if no errors are returned then overwrites listdata to filename


def run():
    # to test my functions :)
    testt = 'tests/'
    test = read_csv(testt + 'test.csv', True)
    print('\n' + str(test))
    print(test[0]['row'] + ', ' + test[0]['col1'] + ', ' + test[0]['col2'] + ', ' + test[0]['col3'] + ', ' + test[0][
        'yo'])
    print(test[1]['row'] + ', ' + test[1]['col1'] + ', ' + test[1]['col2'] + ', ' + test[1]['col3'] + ', ' + test[1][
        'yo'])
    print(test[2]['row'] + ', ' + test[2]['col1'] + ', ' + test[2]['col2'] + ', ' + test[2]['col3'] + ', ' + test[2][
        'yo'])
    print(find_csv_record(testt + 'test.csv', '002', key='yo'))
    print(update_csv_record(testt + 'test.csv', True, 1, 'col2', 'col2updated'))
    print(read_csv(testt + 'test.csv', True))
    print(append_csv_record(testt + 'test.csv', ['1', '2', '3', '4', '5']))
    print(read_csv(testt + 'test.csv', True))
    print(write_csv_record(testt + 'test2.csv',
                           [['row', 'col1', 'col2'], ['row', 'col1', 'col2'], ['row', 'col1', 'col2']]))
    print(read_csv(testt + 'test2.csv', False))
    print(read_csv(testt + 'CSVTestData.csv', True))
    print(read_csv(testt + 'CafeTestData.csv', True))
    print(exist(testt + 'test.csv'))
    print(insert_csv_record(testt + 'test.csv', [6, 7, 8, 9, 10], 6))


if __name__ == '__main__':
    run()
