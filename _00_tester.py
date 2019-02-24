
from _15_BinaryConverterAndStuff import dec2bin


def run():
    print('hi.76.sdf..345'.count('.'))
    loop = True
    while loop:
        print(dec2bin(input('decimal: ')))
        loop = str(input('Restart? (y/n)')).lower() == 'y'


if __name__ == '__main__':
    run()
