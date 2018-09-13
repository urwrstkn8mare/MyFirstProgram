import os

name = os.path.realpath(__file__)
logr = input('LOG (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
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


def exist(filename):
    # Tries to open file which name is stored in the parameter, 'filename'.
    try:  # Tries...
        open(str(filename))
    except FileNotFoundError:
        return False
    # If there is a FileNotFoundError than return False...
    return True
    # ...otherwise return True.


def read_csv(filename, header):  # Define function read_csv with parameters: filename and header.
    # This function checks for multiple csv file formatting requirements such as ignoring commas between quotation marks
    # and returns a list with dictionaries inside representing each line. If header is True then you can call fields by
    # it's header.
    lognm = ' - read_csv()'
    while True:  # Infinitely loop the following until broken.
        if filename.endswith('.csv'):  # If variable filename's string ends with '.csv' then...
            try:
                with open(str(filename),
                          'r') as fr:  # ...try to open file which name is stored in variable filename as fr.
                    content = fr.readlines()  # Store list containing each line in the opened file, fr, as a list item.
                    content = [xx.strip() for xx in
                               content]  # Removes whitespace (eg. ' ', '\n') from each line in list variable content.
            except FileNotFoundError:  # If there is an error, FileNotFoundError, then...
                return error(name, '01_FILENOTFOUND',
                             'The file you gave was not found or there was a problem with the program. (the file must '
                             'be in the same directory as this program.)')  # return a custom error.
            if not content:
                return error(name, '02_EMPTY', 'The file contains nothing.')
            else:
                for i in range(
                        len(content)):  # While variable i is in the range of the number of list items in content...
                    if ',' not in content[i]:  # If there is not a ',' in variable i of content...
                        return error(name, '03_FORMATERROR',
                                     'Not formatted correctly according to CSV format.')  # ..return a custom error.
                log('VERIFIED', logr, name=lognm)  # Log 'VERIFIED' if logr is True.
                pp = []  # Store an empty list in variable pp.
                log('LOOP x', logr, name=lognm)  # Log 'LOOP X' if logr is true.
                log(len(content), logr, name='len(content)' + lognm)
                for x in range(
                        len(content)):  # While variable x is in the range of the number of list items in content...
                    xx = content[x].split(
                        ',')  # ...split x of content around the commas and store the list output in variable xx.
                    b = []  # Store an empty list in variable b.
                    log('LOOP c', logr, name=lognm)  # Log 'LOOP C' if logr is True.
                    for c in range(
                            len(xx)):  # While variable c is in the range of the number of items in list variable xx...
                        log('LOOP y', logr, name=lognm)  # ...log 'LOOP Y' if logr is True.
                        for y in range(len(
                                xx)):  # While variable y is in the range of the number of items in the list variable xx...
                            z = ','.join(xx[
                                         c:y + 1])  # ...join variable c to variable y plus 1 of list variable xx with commas and store it in variable z.
                            z = z.strip()  # Remove whitespace (eg. ' ', '\n') from variable z.
                            log(z, logr, name='z' + lognm)  # Log variable z if logr is True and with the name: 'z'.
                            log(str(z.startswith('\"')), logr,
                                name='z.startswith(\'\"\')' + lognm)  # Log True if z starts with '"' if logr is true and with the name: 'z.startswith('"')'.
                            log(str(z.endswith('\"')), logr,
                                name='z.endswith(\'\"\')' + lognm)  # Log True if z ends with '"' if logr is true and with the name: 'z.endswith('"')'.
                            if z.startswith('\"') and z.endswith('\"'):  # If z starts with and ends with '""' then...
                                log(str([c, y + 1]), logr,
                                    name='[c, y + 1]' + lognm)  # ...log list containing c and y plus 1 if logr is True and with the name: '[c, y + 1]'.
                                b.append([c, y + 1])  # Append list containing c and y plus 1 to list variable b.
                    b.append([-1, -1])  # Append list containing negative 1 and negative 1 to list variabel b.
                    log(str(b), logr, name='b' + lognm)  # Log variable b if logr is True with the name: 'b'.
                    p = []  # Store empty list in variable p.
                    m = 0  # Store zero in variable m.
                    u = 0  # Store zero in variable u.
                    log(len(xx), logr,
                        name='len(xx)' + lognm)  # Log the number of items in xx if logr is True with the name: 'len(xx)'.
                    log('LOOP U', logr, name=lognm)  # Log 'LOOP U' if logr is True.
                    while u < len(xx):  # While u is under the number of items in xx...
                        if u == b[m][0]:  # ...,if u is the same as 0 of m of b then...
                            o = ','.join(
                                xx[
                                u:b[m][1]])  # ...join u to 1 of m of b of with commas and then store it in variable o.
                            o = o.strip()[1:-1]
                            log(o, logr,
                                name='o (True)' + lognm)  # Log variable o if logr is True with the name: 'o (True)'.
                            u = b[m][1]  # Store 1 of m of b in variable u.
                            log(u, logr,
                                name='u (True)' + lognm)  # Log variable u if logr is True with the name: 'u (True)'.
                        else:  # Else...
                            o = xx[u]  # ...store u of xx in o.
                            log(o, logr,
                                name='o (False)' + lognm)  # Log variable o if logr is True with the name: 'o (False)'.
                            u += 1
                            log(u, logr,
                                name='u (False)' + lognm)  # Log variable u if logr is True with the name: 'u (False)'.
                        p.append(o.strip())  # Append o with whitespace removed to p.
                    log(p, logr, name='pp' + lognm)  # Log variable p if logr is True with the name: 'p'.
                    pp.append(p)  # Append p to list pp.
                    log(pp, logr, name='pp' + lognm)  # Log variable pp if logr is True with the name: 'pp'.
                old = len(pp[0])  # Store the number of items in 0 of pp in old.
                log('LOOP H', logr, name=lognm)  # Log 'LOOP H' if logr is True.
                for h in range(len(pp)):  # While h is in the range of the number of items in pp...
                    new = len(pp[h])  # ...store the number of items in h of pp in variable new.
                    log(old, logr, name='old' + lognm)  # Log variable old if logr is True with the name: 'old'.
                    log(new, logr, name='new' + lognm)  # Log variable new if logr is True with the name: 'new'.
                    if old == new:  # If old is the same as new...
                        old = new  # Store new in old.
                    else:  # Else...
                        return error(name, '04_FORMATERROR',
                                     'Not formatted correctly according to CSV format.')  # ...return a custom error.
                log(pp, logr, name='pp' + lognm)  # Log variable pp if logr is True with the name: 'pp'.
                keys = []  # Store an empty list in keys.
                csvfile = []  # Store an empty list in csvfile.
                log('LOOP G', logr, name=lognm)  # Log 'LOOP G' if logr is True.
                q = 0
                for g in range(len(pp[0])):  # While g is in the range of the number of items in 0 of pp...
                    if header:  # ...if header is true then...
                        keys.append(pp[0][g])  # ...append g of 0 of pp to keys.
                    else:  # Else...
                        keys.append(g)  # ...append g to keys.
                if header:
                    q = 0
                log(keys, logr, name='keys' + lognm)  # Log variable keys if logr is True with the name: 'keys'.
                log(header, logr, name='header' + lognm)  # Log variable header if logr is True with the name: 'header'.
                log('LOOP Q', logr, name=lognm)  # Log 'LOOP Q' if logr is True.
                while q < len(pp):  # While q is under the number of items in pp...
                    b = {}  # ..store an empty dictionary in b.
                    for j in range(len(pp[q])):  # While j is in the range of the number of q of pp...
                        b[keys[j]] = pp[q][j]  # ...store j of q of pp in j of keys, of b.
                    csvfile.append(b)  # Append b to csvfile.
                    q += 1  # Add one to q.
                log(csvfile, logr,
                    name='csvfile' + lognm)  # Log variable csvfile if logr is True with the name: 'csvfile'.
                return csvfile  # Return variable csvfile.
        else:  # Else...
            return error(name, '05_EXTENSION', 'The file does not have a .csv extension.')  # ...return a custom error.


def find_csv_record(filename, key_value, **opt):
    # This function finds the row which key is the key_value specified.
    # This function has the parameters: filename, key_value and an optional parameter, 'key'.
    csvfile = read_csv(filename, True)
    # Call read_csv with its filename parameter as this own function's filename paramter and header parameter with True.
    if not isinstance(csvfile, list):
        if csvfile.startswith('!ERROR'):
            return csvfile
    if 'key' in opt:
        keyy = opt['key']
    else:
        keyy = 'key'
    # If there is the optional parameter, 'key', is present then store the value of the parameter in variable keyy otherwise store 'key'.
    for l in range(len(csvfile)):
        try:
            if csvfile[l][keyy] == str(key_value):
                if 'output' in opt:
                    if opt['output'] == 'rownum':
                        return int(l)
                    elif opt['output'] == 'row':
                        return csvfile[l]
                    else:
                        return error(name, '06_BADPARAM',
                                     'The optional parameter, output, did not have or had an incorrect value.')
                else:
                    return csvfile[l]
            # If row, l, and field, keyy, is the same as the parameter, key_value.
            else:
                return error(name, '06.5_NOTFOUND', 'Could not find paramter.')
        except IndexError:
            return error(name,
                         '07_NOKEY',
                         'CSV not formatted correctly to be used by this program.\nThere must be header and header '
                         'must have a key field to use.')
            # If there is an IndexError than return a custom error.


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
                            if ',' in str(inside[d][n]):
                                tmp.append('\"' + str(inside[d][n]) + '\"')  # appends string form of n of d of inside
                            else:
                                tmp.append(str(inside[d][n]))  # appends string form of n of d of inside
                        f.write(', '.join(
                            tmp) + '\n')  # joins together items in tmp with comma and writes it to the file. Adds a new line after.
                    else:  # else returns error
                        return error(name,
                                     '08_NUMBEROFLINES',
                                     'Lines do not have same number of fields. (The file may be incomplete or corrupted.)')
                else:  # else returns error
                    return error(name,
                                 '09_NOLIST',
                                 'Parameters other than filename should be lists. (The file may be incomplete or corrupted.)')
        except IndexError:  # if there is an index error closes file and returns error
            f.close()
            return error(name, '10_BADPARAM',
                         'Parameters were incorrectly inputted. (The file may be incomplete or corrupted.)')
        f.close()  # closes file


def update_csv_record(filename, header, row, field, new_value):
    # This function updates a specific value in the csv file with new value sepcified in new_value.
    csvfile = read_csv(filename, header)
    # Call read_csv with its filename parameter as this own function's filename paramter and header parameter with this own functions's parameter, header.
    if not isinstance(csvfile, list):
        if csvfile.startswith('!ERROR'):
            return csvfile
    try:
        try:
            csvfile[row][field] = str(new_value)
        except TypeError:
            return error(name, '010.5_NOTSTR', 'Row cannot be a str.')
        # Tries to value in the specified row and field with the new_value.
    except IndexError:
        return error(name, '11_PARAMPROB', 'Row and field are not found in file.')
        # If it returns an IndexError than output a custom error.
    if ',' in str(new_value):
        csvfile[row][field] = str('\"' + str(new_value) + '\"')
    newfile = []
    log(newfile, logr, name='newfile')
    # Variable newfile is initialised with the first row (header row) of csvfile joined together with commas.
    for l in range(len(csvfile)):
        ll = ','.join(csvfile[l])
        ll = ll.split(',')
        pp = []
        for g in range(len(ll)):
            pp.append(csvfile[l][ll[g]])
        newfile.append(pp)
    # For every line turn the dictionary into a list and append it to newfile.
    write_csv_record(filename, newfile)


def append_csv_record(filename, listt):
    if isinstance(listt, list):  # checks if listt is a list
        csvfile = read_csv(filename, False)  # reads filename with no headers and outputs into csvfile
        try:
            if len(listt) == len(csvfile[
                                     0]):  # checks if the number of items in listt is the same as the number of items in 0 of csvfile.
                with open(filename, 'a') as f:  # opens filename
                    tmp = []
                    for n in range(len(listt)):
                        if ',' in str(listt[n]):
                            tmp.append('\"' + str(listt[n]) + '\"')
                        else:
                            tmp.append(str(listt[n]))
                    f.write(', '.join(tmp) + '\n')
                    f.close()
            else:  # else returns error
                return error(name,
                             '12_BADNEWROW',
                             'CSV file will not be formatted correctly with this new row. (The number of fields in input '
                             'is not the same as file inputted)')
        except IndexError:
            if csvfile.startswith('!ERROR'):
                return csvfile
            else:
                error(name, '12.5', 'There wasn\'nt an error and there was not a list. Confused.')
    else:  # else returns error
        return error(name, '13_NOLIST', 'Parameter list is not a list. (it should be)')


def insert_csv_record(filename, listt, index):
    if isinstance(listt, list):  # checks if listt is a list
        data = read_csv(filename, False)  # reads file and outputs into data
        try:
            if len(listt) == len(data[
                                     0]):  # checks if the number of items in listt is the same as the number of items in 0 of data.
                listdata = []  # creates empty list, listdata
                for i in range(len(data)):  # while i is in the number of items in data
                    tmpitem = []  # creates emptyl list, tmpitem
                    for n in range(len(data[i])):  # while n is in the number of items in i of data
                        tmpitem.append(data[i][n])  # appends to tmpitem n of i of data
                    listdata.append(tmpitem)  # appends tmpitem to listdata
                tmp = []
                for n in range(len(listt)):
                    if ',' in str(listt[n]):
                        tmp.append('\"' + str(listt[n]) + '\"')
                    else:
                        tmp.append(str(listt[n]))
                listdata.insert(int(index), tmp)  # inserts listt at index into listdata
                for b in range(len(listdata)):  # while b is in the number of items in listdata
                    if not len(listdata[b]) == len(
                            listdata[0 - (len(listdata) - b)]):  # checks if the number of items in b of
                        # listdata is not equal to the number of items in (0 - len(listdata) - b) of listdata). Also returns error after
                        return error(name, '14_INCORRECT',
                                     'New line does not have the same amount of fields as other lines.')
                write_csv_record(filename, listdata)  # if no errors are returned then overwrites listdata to filename
            else:  # else returns error
                return error(name,
                             '12_BADNEWROW',
                             'CSV file will not be formatted correctly with this new row. (The number of fields in input '
                             'is not the same as file inputted)')
        except IndexError:
            if data.startswith('!ERROR'):
                return data
            else:
                error(name, '12.5', 'There wasn\'nt an error and there was not a list. Confused.')
    else:
        return error(name, '14.5_NOLIST', 'Parameter list is not a list. (it should be)')


def run():
    print('MAINLINE')
    thefile = 'tests/08_SamitShaikh_updatedfile.csv'
    update_csv_record(thefile, True, find_csv_record(thefile, 1, key='ID', output='rownum'), 'SEM1', 87)
    update_csv_record(thefile, True, find_csv_record(thefile, 'Chris', key='GNAME', output='rownum'), 'GNAME',
                      'Christopher')
    append_csv_record(thefile, [4, 'Humpty', 'Dumpty', 0, 35, 35, 'D', 'Started Late'])
    print(read_csv(thefile, True))


if __name__ == '__main__':
    run()
