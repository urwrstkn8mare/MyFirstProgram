# Yr8CS1_Samit Shaikh_20180510

import random


def checkmoduleguess(guessed, randomised, triess):
    global guesstriesss
    if guessed == randomised:
        triess = triess + 1
        print('Congrats! You guessed the number in ' + str(triess) + ' tries!')
        guesstriesss = 4
    elif guessed > randomised:
        print('Too high!')
        guesstriesss = 1
    elif guessed < randomised:
        print('Too low!')
        guesstriesss = 1
    else:
        print('I do not know what you gave me. ')
        print('Too bad! I will still count this as a try!! (note: numbers only)')
    return guesstriesss


def GuessTheNumber():
    global guess
    print('Welcome to the Guess the Number Game!')
    print('Can you guess the number I randomly chose between 1 and 100??')
    randomnumber = int(random.randint(1, 100))
    difficulty = str(input('Set difficulty (high/low) : '))
    print('')
    print('Try!')
    print('')
    guesstries = 2
    tries = 0
    if difficulty == 'low':
        while 3 > guesstries > 0:
            try:
                guess = int(input('Guess -> '))
            except ValueError:
                print('! ERROR ! Must enter INTEGER\nExiting...')
                exit()
            print('')
            guesstries = checkmoduleguess(guess, randomnumber, tries)
            tries = tries + 1
        print('Game ending...')
    elif difficulty == 'high':
        while 3 > guesstries > 0 and tries < 41:
            try:
                guess = int(input('Guess -> '))
            except ValueError:
                print('! ERROR ! Must enter INTEGER\nExiting...')
                exit()
            print('')
            guesstries = int(checkmoduleguess(guess, randomnumber, tries))
            tries = tries + 1
        if tries == 30:
            print('You have no more tries! The number you should have guessed was ' + str(randomnumber) + '!')
            print('Too bad! Game ending...')
        else:
            triesoppo = 30 - tries
            print('And you had ' + str(triesoppo) + ' tries left!')
            print('Game Ending...')
    else:
        print('Incorrect answer. Ending...')
    return


def run():
    GuessTheNumber()


if __name__ == '__main__':
    run()
