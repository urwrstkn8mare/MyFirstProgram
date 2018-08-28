linecounter = 1  # sets variable linecounter to 1
logr = input('LOG (True/False): ')  # sets boolean logr to to user assigned bool (for logging purposes)
print()
if logr.lower() == 'true':
    logr = True
else:
    logr = False


def log(text):
    global logr
    global linecounter
    if logr:
        print('LOG>>> ' + str(text) + ' <<< ' + str(linecounter))
        linecounter += 1
    else:
        pass
    return


def error(err, string):
    print(err + ' ' + string)
    input('Enter to continue...')
    return err


def read_csv(filename, header):
    while True:
        if filename.endswith('.csv'):
            global content
            try:
                with open(str(filename)) as fr:
                    content = fr.readlines()
                    content = [xx.strip() for xx in content]
            except FileNotFoundError:
                return error('!ERROR_02!',
                             'The file you gave was not found or there was a problem with the program. (the file must '
                             'be in the same directory as this program.)')
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
                keys.append(g + 1)
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
            error(
                '!ERROR! CSV not formatted correctly to be used by this program.\nThere must be header and header '
                'must have a key field to use.')


def update_csv_record(filename, header, row, field, new_value):
    csvfile = read_csv(filename, header)
    log('csvfile -> ' + str(csvfile))
    try:
        csvfile[row][field] = new_value
    except IndexError:
        error('!ERROR! Row and field are not found in file.')
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
    if type(listt) == type([]):
        csvfile = read_csv(filename, False)
        if len(listt) == len(csvfile[0]):
            f = open(filename, 'a')
            f.write(', '.join(listt))
            f.close()
        else:
            error(
                '!ERROR! CSV file will not be formatted correctly with this new row. (The number of fields in input '
                'is not the same as file inputted)')
    else:
        error('!ERROR! Parameter list is not a list. (it should be)')


def write_csv_record(filename, inside):
    f = open(filename, 'w')
    try:
        old = len(inside[0])
        for d in range(len(inside)):
            if type(inside[d]) == type([]):
                new = len(inside[d])
                if old == new:
                    f.write(', '.join(inside[d]) + '\n')
                else:
                    error('!ERROR! Lines do not have same number of fields. (The file may be incomplete or corrupted.)')
            else:
                error(
                    '!ERROR! Parameters other than filename should be lists. (The file may be incomplete or corrupted.)')
    except IndexError:
        f.close()
        error('!ERROR! Parameters were incorrectly inputted. (The file may be incomplete or corrupted.)')
    f.close()


def run():
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


if __name__ == '__main__':
    run()
