from _15_BinaryConverterAndStuff import *
from _19_InterpreterForCSV import error
import os

name = os.path.realpath(__file__)


def parse(string):
    if isinstance(string, str):
        string = string.strip()
        intrange = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        log(string[1], logr)
        log(string[-2], logr)
        log(string[-1], logr)
        if '=' == string[-1] and string[0] in intrange:
            operators = ['+', '-', '/', '*']
            optdict = {
                operators[0]: lambda fst, lst: fst + lst,
                operators[1]: lambda fst, lst: fst - lst,
                operators[2]: lambda fst, lst: fst / lst,
                operators[3]: lambda fst, lst: fst * lst
            }
            for i in range(len(operators)):
                if operators[i] in string:
                    tmp = string[0:-1]
                    tmp = tmp.split(operators[i])
                    try:
                        first = float(tmp[0].strip())
                        second = float(tmp[1].strip())
                    except ValueError:
                        return error(name, '02valueerror',
                                     'The values outside the ' + operators[i] + ' and = must be integers.')
                    return optdict[operators[i]](first, second)
            return error(name, '03_nooperators', 'No of the eligble operaters were found in the string.')
        else:
            return error(name, '04_invalidstr',
                         'The string does not end with a =, start with an integer or have the second last character as an integer.')
    else:
        return error(name, '01nolist', 'The inputted string parameter is not in string format. <parse(string)>')


def txtarith(file):
    data = readfileval(file)
    output = []
    for l in range(len(data)):
        tmp = parse(data[l].strip())
        if not str(tmp).startswith('!ERROR'):
            output.append(data[l] + str(tmp))
        else:
            return tmp
    with open(file, 'w') as f:
        f.write('\n'.join(output))
    f.close()


def run():
    print(txtarith('tests/test4arith.txt'))
    print(parse('3.5+0.5='))


if __name__ == '__main__':
    run()
