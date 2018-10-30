# magic coin machine challenge
def run():
    print('')
    print('Part A:')
    inputvar = input('You are digging in your Grandparent’s backyard and uncover a bag of how many gold coins?')
    print('Ok. So you dug up ' + inputvar + ' coins.')
    inputvar2 = input('The next day you sneak into your Grandfathers shed and stick the coins inside his steam-powered '
                      'replicating invention. You hear a whiz and a pop and a few hours later, out shoots how many '
                      'coins?')
    inputvar3 = input('And how many days until you check your treasure chest again?')
    newnumber = int(inputvar) + int(inputvar2) * int(inputvar3)
    newnumber = str(newnumber)
    print('So if you did this for ' + str(inputvar3) + ' days you would get ')
    print(newnumber + ' coins in your treasure chest!')
    print('')
    print('Part B:')
    print('Your nasty next door neighbour’s Raven watches you take the gold coins home ')
    print('every day and place them in your bedroom. The Raven likes your shiny gold')
    inputvar4 = input('coins and no matter what you do, it always manages to steal how many coins from you each week?')
    newnumber = int(newnumber) - int(inputvar3) / 3 * int(inputvar4)
    newnumber = str(newnumber)
    print('So, at the end of the year you will have ' + newnumber + ' coins.')
    print('')
    print('Part C:')
    print('You figure out a way to stop the Raven from stealing ' + inputvar4 + "coins but by the end of the week the "
                                                                                "sneaky thief has found another way to "
                                                                                "your coins and now steals 2 coins per "
                                                                                "week. And on top of that, "
                                                                                "your Grandfather being a constant "
                                                                                "tinkerer has fiddled with the "
                                                                                "steam-powered replicator and now it "
                                                                                "only "
                                                                                "produces 5 coins per week.")
    newnumber = int(inputvar) + 5 * int(inputvar3)
    newnumber = int(newnumber) - 52 * 2
    newnumber = str(newnumber)
    print('So now instead you will have ' + newnumber + ' coins.')
    print('')

    if __name__ == '__main__':
        run()
