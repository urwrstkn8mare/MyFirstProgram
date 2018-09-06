logr = input('LOG (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                               'uh-huh']  # If userinput is in the list then variable logr is True
print()  # Print new line


def log(name, text, validation):  # Define function log with parameters: name, text and validation
    if validation:  # If variable validation is True then...
        print(
            'LOG>>> ' + str(text) + ' <<< ' + str(name))  # ... print 'LOG>>>', variable text, '<<<' then variable name.


def error(err, string):  # Define function error with parameters: err and string
    print(err + ' ' + string)  # Print variables err and string with a space in between.
    return err  # Return variable err.


def exist(filename):
    try:
        open(str(filename))  # tries to open file
    except FileNotFoundError:
        return False  # if error then returns false
    return True  # else returns true


def read_csv(filename, header):
    while True:  # infinite loop unless breaked
        if filename.endswith('.csv'):  # if filename ends with '.csv'
            try:
                with open(str(filename)) as fr:  # tries to read filename
                    content = fr.readlines()
                    content = [xx.strip() for xx in content]  # strips whitespace
            except FileNotFoundError:  # if file not found then outputs custom error
                return error('!ERROR_02!',
                             'The file you gave was not found or there was a problem with the program. (the file must '
                             'be in the same directory as this program.)')  #
            for i in range(len(content)):
                if content[i].find(',') == -1:
                    return error('!ERROR_03!', 'Not formatted correctly according to CSV format.')
            log('VERIFIED')
            pp = []
            log('LOOP X')
            for x in range(len(content)):
                xx = content[x].split(',')
                b = []
                log('LOOP C')
                for c in range(len(xx)):
                    log('LOOP Y')
                    for y in range(len(xx)):
                        z = ','.join(xx[c:y + 1])
                        z = z.strip()
                        log('zandmore -> ' + z + str(z.startswith('\"')) + str(z.endswith('\"')))
                        if z.startswith('\"') and z.endswith('\"'):
                            log('[c, y + 1] -> ' + str([c, y + 1]))
                            b.append([c, y + 1])
                b.append([-1, -1])
                log('b -> ' + str(b))
                p = []
                m = 0
                u = 0
                log('len(xx) -> ' + str(len(xx)))
                log('LOOP U')
                while u < len(xx):
                    if u == b[m][0]:
                        o = ','.join(xx[u:b[m][1]])
                        log('join -> ' + ','.join(xx[u:b[m][1]]))
                        u = b[m][1]
                        log('u -> ' + str(u))
                    else:
                        o = xx[u]
                        log('xx[u] -> ' + xx[u])
                        u += 1
                    p.append(o.strip())
                log('p -> ' + str(p))
                pp.append(p)
                log('pp -> ' + str(pp))
            old = len(pp[0])
            log('LOOP H')
            for h in range(len(pp)):
                new = len(pp[h])
                log('old -> ' + str(old))
                log('new -> ' + str(new))
                if old == new:
                    old = new
                else:
                    return error('!ERROR_04!', 'Not formatted correctly according to CSV format.')
            log('pp -> ' + str(pp))
        else:
            return error('!ERROR_01!', 'The file does not have a .csv extension.')
        keys = []
        csvfile = []
        log('LOOP G')
        for g in range(len(pp[0])):
            if header:
                keys.append(pp[0][g])
            else:
                keys.append(g)
        log('keys -> ' + str(keys))
        log('header -> ' + str(header))
        if header:
            q = 1
        else:
            q = 0
        log('LOOP Q')
        while q < len(pp):
            b = {}
            for j in range(len(pp[q])):
                b[keys[j]] = pp[q][j]
            csvfile.append(b)
            q += 1
        log('csvfile -> ' + str(csvfile))
        return csvfile


def find_csv_record(filename, key_value, **key):
    # there must be header and header must have a key field to use
    csvfile = read_csv(filename, True)
    log('csvfile -> ' + str(csvfile))
    if 'key' in key:
        keyy = key['key']
    else:
        keyy = 'key'
    for l in range(len(csvfile)):
        log(l)
        try:
            log('csvfile[l][keyy] -> ' + str(csvfile[l][keyy]))
            log('key_value -> ' + str(key_value))
            if csvfile[l][keyy] == key_value:
                return csvfile[l]
        except IndexError:
            return error(
                '!ERROR! CSV not formatted correctly to be used by this program.\nThere must be header and header '
                'must have a key field to use.')


def update_csv_record(filename, header, row, field, new_value):
    csvfile = read_csv(filename, header)
    log('csvfile -> ' + str(csvfile))
    try:
        csvfile[row][field] = new_value
    except IndexError:
        return error('!ERROR! Row and field are not found in file.')
    log('csvfile -> ' + str(csvfile))
    log('csvfile[row][field] -> ' + str(csvfile))
    newfile = [', '.join(csvfile[0])]
    for l in range(len(csvfile)):
        ll = ','.join(csvfile[l])
        ll = ll.split(',')
        pp = []
        for g in range(len(ll)):
            pp.append(csvfile[l][ll[g]])
        newfile.append(', '.join(pp))
    log('newfile -> ' + str(newfile))
    f = open(filename, "w")
    writeto = ''
    for h in range(len(newfile)):
        writeto = writeto + newfile[h] + '\n'
    log('writeto -> ' + str(writeto))
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
