def vending_machine(newitem, newitemconfirmation):
    print('Welcome to the advanced Vending Machine. I am the first generation of advanced AI called Bob. I have been '
          'put into this vending machine accidentally.')
    print('')
    print('Raw Chicken - 1')
    print('Overcooked Chicken - 2')
    print('McDonalds (the whole company) - 3')
    print('Coke - 4')
    print('Other Soft Drink - 5')
    print('Underwear (You can find me in some vending machines!) - 6')
    print('Chocolate - 7')
    if newitemconfirmation == 1:
        print('{0} - 8'.format(str(newitem)))
    else:
        pass
    request = int(input('What do you choose?'))
    print('')
    if request >= 9 or request <= 0:
        print('Sorry, you have not chosen an appropriate number.')
        print('If you want me to restart than choose 1.')
        print('If you want to add an item to the list than choose 2.')
        request = int(input('Select: '))
        print('')
        if request >= 3 or request <= 0:
            print('Sorry, you have not chosen correctly or there may have been an error.')
            print('Restarting...')
            print('')
            vending_machine('N/A', 2)
        else:
            if request == 1:
                print('Restarting...')
                print('')
                vending_machine('N/A', 2)
            elif request == 2:
                add_item = input('Input the item you wish to add: ')
                print('Restarting with new values...')
                print('')
                vending_machine(add_item, 1)
            else:
                print('Sorry, you have not chosen correctly or there may have been an error.')
                print('Restarting...')
                print('')
                vending_machine('N/A', 2)
    else:
        if request == 1:
            print('Hope you like it! (who likes raw chicken?)')
        elif request == 2:
            print('Ummmm... I have never tasted food. But it does not look good!')
        elif request == 3:
            print('Wow you are rich!. You bought McDonalds and now you have infinite food. (junk food tho, '
                  'but who cares!)')
        elif request == 4:
            print('Wow, you are so normal... (but coke still is good)')
        elif request == 5:
            print('Why not coke? (I guess it is still good!)')
        elif request == 6:
            print('Are you wearing any now. You can put it on now... I will not look, I promise! Wait I don not have '
                  'eyes. :(')
        elif request == 7:
            print('Mmmmm.... Even though I have never tasted chocolate, it looks so good! Enjoy!')
        elif request == 8 and newitemconfirmation == 1:
            print('So you chose ' + newitem + '! Hopefully its good! (It should be, you made it yourself.)')
        else:
            vending_machine('N/A', 2)
    print('Thank you for using this vending machine!')
    print('')
    return


def run():
    vending_machine('N/A', 2)


if __name__ == '__main__':
    run()
