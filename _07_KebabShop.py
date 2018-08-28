from _06_VendingMachine import vendingMachine


def KebabShopRequest():
    print('\nWelcome to the Kebab Shop!')
    order = ['']
    ordertotal = 0
    NumberOfPeople: int = int(input('How many people will I be serving today?'))
    NumberOfPeople = NumberOfPeople + 1
    print('')
    print('Ok. Rememeber that Lamb is 15 Dollars and Chicken is 10 Dollars')
    OrderNumber = 1
    while NumberOfPeople > OrderNumber > 0:
        orderRequest = str(
            input('So you are order number ' + str(OrderNumber) + '. Would you like Lamb Kebab or Chicken Kebab?'))
        if orderRequest == 'lamb':
            order.append('lamb')
            ordertotal = ordertotal + 15
        elif orderRequest == 'chicken':
            order.append('chicken')
            ordertotal = ordertotal + 10
        else:
            print('You did not give an appropriate answer, try again!')
            print('NOTE: you must write either lamb or chicken. No caps just what was just written to you.')
            KebabShopRequest()
        print('')
        OrderNumber = OrderNumber + 1
    print('Here is youre order summary: ')
    OrderNumber = 1
    while NumberOfPeople > OrderNumber > 0:
        print('Order ' + str(OrderNumber) + ': ' + order[OrderNumber])
        OrderNumber = OrderNumber + 1
    print('')
    print('Order Total: $' + str(ordertotal))
    print('')
    print('')
    drinksconfirm = input('Would you like drinks? ')
    if drinksconfirm == 'yes':
        drinks = input('Coke ($2 each) or Pepsi? ($1.50) ')
        if drinks == 'coke':
            drinkprice = 2 * (NumberOfPeople - 1)
        elif drinks == 'pepsi':
            drinkprice = 1.5 * (NumberOfPeople - 1)
        else:
            drinkprice = 0
            print('You did not give appropriate answer. You will not have ordered anything.')
    else:
        print('That is ok!')
        drinkprice = 0
    print('Before you purchase, I would like to remind you that the vending machine is available to you.')
    ordertotal = ordertotal + drinkprice
    print('Youre order total is now: $' + str(ordertotal))
    print('You finished ordering! ')
    vendingquery = input('Do you want to use the vedning machine? ')
    if vendingquery == 'yes':
        print('')
        vendingMachine('N/A', 2)
    else:
        pass
    print('Ok. Have a great day!')
    return


def run():
    KebabShopRequest()


if __name__ == '__main__':
    run()
