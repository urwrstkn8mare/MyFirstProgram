def FCRPriceCalculator():
    name = input('What is your name?')
    age: int = int(input('What is your age, ' + name + '?'))
    if age >= 16 <= 65:
        price: int = 35
    else:
        price = 20
    print('The price is ' + str(price) + ' dollars!')
    return


def run():
    FCRPriceCalculator()


if __name__ == '__main__':
    run()
