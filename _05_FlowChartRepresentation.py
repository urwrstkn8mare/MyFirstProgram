def fcr_price_calculator():
    name = input('What is your name?')
    age: int = int(input('What is your age, ' + name + '?'))
    if age >= 16 <= 65:
        price: int = 35
    else:
        price = 20
    print('The price is ' + str(price) + ' dollars!')
    return


def run():
    fcr_price_calculator()


if __name__ == '__main__':
    run()
