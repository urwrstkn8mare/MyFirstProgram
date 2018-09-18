from _15_BinaryConverterAndStuff import *
from _19_InterpreterForCSV import error
import os
import re

name = os.path.realpath(__file__)

mlog = input('MLOG (True/False): ').lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly',
                                                'uh-huh']  # If userinput is in the list then variable logb is True
print()


def parse(string):
    string = str(string)
    try:
        return float(string)
    except ValueError:
        string = string.strip()
        intrange = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
        log(string[1], mlog)
        log(string[-2], mlog)
        log(string[-1], mlog)
        if string[-1] in intrange and string[0] in intrange:
            operators = ['+', '/', '**', '*', '-']
            optdict = {
                operators[0]: lambda fst, lst: fst + lst,
                operators[1]: lambda fst, lst: fst / lst,
                operators[2]: lambda fst, lst: fst ** lst,
                operators[3]: lambda fst, lst: fst * lst,
                operators[4]: lambda fst, lst: fst - lst
            }
            for i in range(len(operators)):
                if operators[i] in string:
                    if string.count(operators[i]) > 1 and not operators[i] == '-':
                        return error(name, '06_toomcuhop', 'Too much operations.')
                    else:
                        log(operators[i], mlog, name='operators[i]')
                        tmp = str(string.strip()).replace(operators[i], '-', 1)
                        if not operators[i] == '-':
                            tmp = tmp.replace(operators[i], '')
                        tmp = tmp.split('-')
                        parts = [tmp[0], tmp[1]]
                        log(tmp, mlog, name='tmp')
                        for z in range(len(tmp)):
                            tmp[z] = tmp[z].strip()
                        if 5 > len(tmp) > 2 and '-' in string[0:-1]:
                            if len(tmp) == 4:
                                parts = ['-'.join(tmp[0:2]).strip(), '-'.join(tmp[2:4]).strip()]
                            elif len(tmp) == 3:
                                if tmp[0].strip() in intrange:
                                    parts = [tmp[0].strip(), '-'.join(tmp[1:3]).strip()]
                                else:
                                    parts = ['-'.join(tmp[0:2]).strip(), tmp[2].strip()]
                        try:
                            log(parts, mlog, name='parts')
                            first = float(parts[0].strip())
                            second = float(parts[1].strip())
                        except ValueError:
                            return error(name, '02valueerror',
                                         'The values outside the ' + operators[i] + ' and = must be integers.')
                        log(operators[i], mlog, name='operators[i] #2')
                        try:
                            return float(optdict[operators[i]](first, second))
                        except ZeroDivisionError:
                            return error(name, '01_zerodevisionerror', 'Cannout divide by zero.')
            return error(name, '03_nooperators', 'No of the eligble operaters were found in the string.')
        else:
            return error(name, '04_invalidstr',
                         'The string does not end with a =, start with an integer or have the second last character as an integer.')


def parse2(string):
    # this doesn't support negative numbers yet or powers
    if '**' in string:
        return error(name, '08_power', 'power not supported.')
    string = string.replace(' ', '')
    intrange = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    stringg = re.split('\+|-|\*\*|\*|/', str(string))
    log(stringg, mlog, name='stringg')
    stringtmp = string
    for l in range(len(stringg)):
        tmpp = stringg[l].strip()
        for c in range(len(tmpp)):
            if not tmpp[c] in intrange:
                return error(name, '07_notint', 'Only floats allowed (no negatives yet).')
        stringtmp = stringtmp.replace(stringg[l], '')
    y = 1
    old = stringg[0]
    while y in range(len(stringg)):
        log('-------', mlog, name='sep')
        e = stringtmp[y - 1]
        log(old, mlog, name='sep')
        log(e, mlog, name='sep')
        log(stringg[y], mlog, name='sep')
        log(string, mlog, name='sep')
        old = parse(str(str(old) + str(e) + str(stringg[y])))
        y += 1
    return float(old)


def txtarith(file):
    data = readfileval(file)
    output = []
    for l in range(len(data)):
        if data[l].strip()[-1] == '=':
            tmp = parse(data[l].strip().replace('=', ''))
        else:
            tmp = error(name, '05_equalno', 'No ending equal sign.')
        output.append(data[l] + str(tmp))
    file = file.replace('.txt', 'output.txt')
    with open(file, 'w+') as f:
        f.write('\n'.join(output))
    f.close()


def run():
    txtarith('tests/ArithmeticExpressionsInput.txt')


if __name__ == '__main__':
    run()
