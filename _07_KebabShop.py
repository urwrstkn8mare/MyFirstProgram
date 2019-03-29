from _06_VendingMachine import vending_machine


def kebab_shop_request():
    print('\nWelcome to the Kebab Shop!')
    order = ['']
    ordertotal = 0
    number_of_people: int = int(input('How many people will I be serving today?'))
    number_of_people = number_of_people + 1
    print('')
    print('Ok. Remember that Lamb is 15 Dollars and Chicken is 10 Dollars')
    order_number = 1
    while number_of_people > order_number > 0:
        order_request = str(
            input('So you are order number ' + str(order_number) + '. Would you like Lamb Kebab or Chicken Kebab?'))
        if order_request == 'lamb':
            order.append('lamb')
            ordertotal = ordertotal + 15
        elif order_request == 'chicken':
            order.append('chicken')
            ordertotal = ordertotal + 10
        else:
            print('You did not give an appropriate answer, try again!')
            print('NOTE: you must write either lamb or chicken. No caps just what was just written to you.')
            kebab_shop_request()
        print('')
        order_number = order_number + 1
    print('Here is you\'re order summary: ')
    order_number = 1
    while number_of_people > order_number > 0:
        print('Order ' + str(order_number) + ': ' + order[order_number])
        order_number = order_number + 1
    print('')
    print('Order Total: $' + str(ordertotal))
    print('')
    print('')
    drinksconfirm = input('Would you like drinks? ')
    if drinksconfirm == 'yes':
        drinks = input('Coke ($2 each) or Pepsi? ($1.50) ')
        if drinks == 'coke':
            drinkprice = 2 * (number_of_people - 1)
        elif drinks == 'pepsi':
            drinkprice = 1.5 * (number_of_people - 1)
        else:
            drinkprice = 0
            print('You did not give appropriate answer. You will not have ordered anything.')
    else:
        print('That is ok!')
        drinkprice = 0
    print('Before you purchase, I would like to remind you that the vending machine is available to you.')
    ordertotal = ordertotal + drinkprice
    print('You\'re order total is now: $' + str(ordertotal))
    print('You finished ordering! ')
    vendingquery = input('Do you want to use the vending machine? ')
    if vendingquery == 'yes':
        print('')
        vending_machine('N/A', 2)
    else:
        pass
    print('Ok. Have a great day!')
    return


def run():
    kebab_shop_request()


if __name__ == '__main__':
    run()
