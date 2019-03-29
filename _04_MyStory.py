import random


def end_story():
    print('The End')
    print('')
    print('')
    restart_story = input('Do you want to restart?')
    if restart_story == 'yes':
        print('')
        story()
    elif restart_story == 'no':
        print('The Story Project has ended!')
        print('')
    else:
        print('You did not choose with correct terms, but the project will end anyway. Bye!')
        print('NOTE: You\'re answer may have been suitable but you must write either no or yes. As written in this '
              'sentence.')


def part2():
    print('Part 2 - Aliens has not finished yet. Sorry...')


def story():
    global ageLong
    global ageNumber
    print('NOTE: All answers must be in lowercase.')
    print('')
    name = input('Hello! Welcome to your story! What is your name?')
    gender = input('Are you female or male?')
    name2 = 'N/A'
    place = input('Do you live in America or North Korea?')
    ageNumber = int(input('How old are you?'))
    setting = input('What year is it?')
    setting = int(setting)
    game = input('Fortnite or Player Unknown Battlegrounds?')
    food = input('What food do you like?')
    weapon = input('What is your favourite weapon?')
    print('')
    if ageNumber > 30:
        ageLong = 'long'
    elif ageNumber <= 30:
        ageLong = 'short'
    else:
        print('You did not choose an appropriate age. Please start again...')
        story()
    if gender == 'female':
        name2 = 'Jemma'
    elif gender == 'male':
        name2 = 'John'
    else:
        print('You did not give an appropriate answer. Please start again...')
        story()
    if place == 'america':
        if 18 > ageNumber:
            print('You have voted to nuke North Korea. You are proud. Then you feel guilt. Guilt about the people you '
                  'killed.')
            print('"They may not have known?" you thought.')
            print()
        elif ageNumber < 18:
            between_age = 30 - int(ageNumber)
            between_age = str(between_age)
            print(
                'You urge mom and dad to vote to destroy North Korea. They say they do not have a say. You do not '
                'believe that! In ' + between_age + ' years you turn 30. Then you become the youngest president ever! '
                                                    'The first move you make as president is to completely wipe North '
                                                    'Korea off the map! South Korea is now an island.')
            print(
                'After that. You face many assassination attempts. You have OP Secret Service so you dodge it. Then '
                'after years of backlash you lead a norm life.')
            print('')
            end_story()
        else:
            print('You did not choose an age. Please start again...')
            story()
    elif place == 'north korea':
        if 18 < ageNumber:
            if setting > 2018:
                print(
                    'North Korea was obliterated in late 2018. You were born before that. You were there. You watched '
                    'North Korea be obliterated by raining nukes. You hate Donald Trump now. After you flee in time '
                    'the only consequences is your new 20th toe!')
                print(
                    'Now you are undercover in America. You\'re name is not {0} anymore but it is now {1}.'.format(name, name2))
                kill = input('Do you want to kill Donald Trump now?')
                print('')
                if kill == 'no':
                    print('You decided to not kill Trump. Too bad, he finds you and kills you. You lived a ' + ageLong +
                          ' ' + ' life!')
                    end_story()
                elif kill == 'yes':
                    print('You kill Trump with a ' + weapon + ' . After you do not no what happens yet...')
                    print('')
                    if random.randint(1, 2) == 1:
                        print('The world congratulates you! You are now president! What do you want to do first?')
                        print('1 - Die')
                        print('2 - Be normal.')
                        print('3 - Take over the world.')
                        president = input('Enter a number: ')
                        president = int(president)
                        if president == 1:
                            print('Bye! You lived a ' + ageLong + ' life!')
                            print('')
                            end_story()
                        elif president == 2:
                            print(
                                'You were a normal president. Nothing happended. The story would be boring so it '
                                'shall end now.')
                            print('')
                            end_story()
                        elif president == 3:
                            p2 = input(
                                'You took over the world. The world was at your command. Then the aliens came... Part '
                                '2 - Aliens?')
                            if p2 == 'yes' or 'Yes' or 'y':
                                print('Let Part 2 - Aliens Begin!')
                                part2()
                            print('')
                        else:
                            print('You did not choose anything. Too bad. Story is going to end.')
                            print('')
                            end_story()
                            return
                    else:
                        print(
                            'The world has decided to hate you. They gave you some ' + food +
                            ' and then they sent you to space.')
                        print(
                            'In space you met aliens. The aliens played a game of chess with you. Then they cut of '
                            'every extruding limb of your body and blended it in a nutri-bullet.')
                        print('')
                        end_story()
                elif kill == 'later':
                    print('Too late. He finds you and kills you. You lived a ' + ageLong + ' life!')
                else:
                    print('You did not choose appropriately. Please start again...')
                    story()
                    return
            elif setting < 2018:
                print(
                    'You should be ashamed! Why would you live in North Korea. I am not even going to continue the '
                    'story. I jump into your universe and shove your ' + food + ' into your face. Then I get your ' +
                    weapon + ' and shoot all your body parts expect your heart and brain. While you bleed to death I '
                             'let you watch ' + game + '!')
                print('')
                end_story()
            else:
                print('You did not choose an appropriate year, please start again...')
                story()
                return
        elif ageNumber < 18:
            if setting > 2018:
                print(
                    'Before you were born. Your country was obliterated. Somehow you are still there. On a small '
                    'island where your country used to be. In that island you are alone. You survive for 3 days. Then '
                    'after not knowing anything, the island get nuked by America. Bye. you lived a ' + ageLong +
                    ' life.')
                print('')
                end_story()
            elif setting < 2018:
                print(
                    'You are too young to understand but you\'re country is bad. You should abandon it now!. The story '
                    'shall not continue until you leave!')
                print('')
                end_story()
            elif setting == 2018:
                print(
                    'You are too young to understand but you\'re country is bad. You should abandon it now!. The story '
                    'shall not continue until you leave!')
                print('')
                end_story()
            else:
                print('You did not choose a appropriate year, please start again...')
                story()
                return
        else:
            print('You did not choose an appropriate age. Please start again...')
            story()
            return
    else:
        print('You did not choose a country. Please start again...')
        story()
        return
    return


def run():
    story()


if __name__ == '__main__':
    run()
