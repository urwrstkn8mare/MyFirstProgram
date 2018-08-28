# PRG10

import random
import sys
import textwrap
import time


def wait_key():
    """Enter to continue."""
    input()
    return


def smartprint(string):
    """Confines text to 44 letters wide."""
    print(textwrap.fill(string, 44))
    return


def newline():
    """Prints a new line"""
    print('')
    return


# noinspection PyUnreachableCode
def theend():
    """The end code, automatically ends script."""
    newline()
    print('THE END!')
    sys.exit()
    return


def line(linelength):
    """Makes a line out of dashs"""
    linedash = '-'
    while len(linedash) < linelength:
        linedash = linedash + '-'
    print(linedash)
    return


def multiplechoice(choice1, choice2, choice3, choice4):
    """Automatically makes a multiple choice box out of arguments"""
    def addspace(choicevaar):
        while len(choicevaar) < 40:
            choicevaar = choicevaar + ' '
        return choicevaar

    newline()
    choice1 = 'A - ' + choice1
    choice2 = 'B - ' + choice2
    choice3 = 'C - ' + choice3
    choice4 = 'D - ' + choice4
    choice1 = '| ' + addspace(choice1) + ' |'
    choice2 = '| ' + addspace(choice2) + ' |'
    choice3 = '| ' + addspace(choice3) + ' |'
    choice4 = '| ' + addspace(choice4) + ' |'
    line(43)
    smartprint(choice1)
    line(43)
    smartprint(choice2)
    line(43)
    smartprint(choice3)
    line(43)
    smartprint(choice4)
    line(43)
    choiceanswer = str(input('-> '))
    line(43)
    choiceloopcheck = 1
    while choiceloopcheck == 1:
        if choiceanswer == 'a' or choiceanswer == 'A':
            choiceanswer = 1
            choiceloopcheck = 2
        elif choiceanswer == 'b' or choiceanswer == 'B':
            choiceanswer = 2
            choiceloopcheck = 2
        elif choiceanswer == 'c' or choiceanswer == 'C':
            choiceanswer = 3
            choiceloopcheck = 2
        elif choiceanswer == 'd' or choiceanswer == 'D':
            choiceanswer = 4
            choiceloopcheck = 2
        else:
            smartprint('You did not give appropriate answer')
            choiceanswer = str(input('  -> '))
            line(43)
            choiceloopcheck = 1
    newline()
    return choiceanswer


def error():
    """Error function"""
    smartprint('! ERROR !')
    smartprint('Ending...')
    theend()
    return


def bossfight(companionstr):
    """Boss fight"""
    newline()
    if companionstr == 'half of your army':
        smartprint(
            'RIP. Half your army was killed by your precious actions, well now you only have half the force. You tried as hard as you can to fight with half your army againt this guardian but ended in failure. After your entire army now slaughtered I had to take you away. I was disssapointed at you for killing of my entire army but I can always get more. Goodbye and stay hungry at home after I wipe your memory.')
        wait_key()
        theend()
    elif companionstr[:13] == 'your friend, ':
        smartprint(
            'Luckily ' + companionstr + ' was there to help you or you would be in defeat. But you were still very weak, but little did you know that your friend was actaully Poseidon, God of the Ocean. He thrusted water from the depths of Antartica and into the guarding, he flew maybe a few miles in the air befor hitting ice, defeated. But the jelly was gone. Dissolved in water, never to be seen again. How dissapointing, I would rather have had you die than lose this treasure but very well, I shall incinerate the both of you.')
        wait_key()
        theend()
    elif companionstr == 'your llama':
        smartprint(
            'Your llama just stood there as you fought. Looking at you and the beast. You screamed for help. It was not until you lost your some limbs he came. He turned giant and squashed the beast into nothingess. Now that\'s my level! I might employ this guy. You retrieved this jelly and now I shall reward you eternal riches and happiness for your now immortal life!')
        wait_key()
        theend()
    elif companionstr == 'your army':
        smartprint('Well that was easy, ' + companionstr + ' thrashed the beast!')
        wait_key()
        theend()
    elif companionstr == 'me':
        smartprint('Well that was easy, ' + 'I' + ' thrashed the beast!')
        wait_key()
        theend()
    else:
        error()


def start():
    """Main story to get to boss fight"""
    smartprint('What is your name?')
    name = str(input('-> '))
    newline()
    smartprint('Welcome to The Incredible Adventures of ' + name + ' and his quest for jelly!')
    smartprint('This is your own adventure!')
    wait_key()
    newline()
    smartprint(
        'You are at home doing nothing but being hungry. You dream of eating many things but nothing as tasty as jelly. Then out of nowhere comes a homeless man!')
    wait_key()
    newline()
    smartprint('What do you say?')
    wahtdoyousay = multiplechoice('You scream and die!',
                                  'You kill him.',
                                  'You ask, "Who are you and what are you doing?"',
                                  'You do nothing')
    newline()
    if wahtdoyousay == 1:
        smartprint('Well that was dumb.')
        wait_key()
        theend()
    elif wahtdoyousay == 2:
        smartprint('Bad move!')
        smartprint(
            'You killed him, but you should not have. He was there to grant you a magnificent quest, you saw him drop a scroll as he fell bleeding to his death. You open it but find it on fire the instant you touch it. You are now cursed. You put your hands togerther. Now you are on fire, dieing. Bad Luck!')
        wait_key()
        theend()
    elif wahtdoyousay == 3:
        smartprint(
            'He replied, "I have been taken away from my home, the street, to give you a message from my master. He asked me to give you this quest," he hanged me a scroll, "you must protect it with your life! You have been assigned a quest. To retreive the acient and legendary, jelly! But be warned, many have died trying. Do you accept this quest?"')
        questaccept = multiplechoice('"YES!"',
                                     '"No way"',
                                     '"Maybe?"',
                                     'Give him money and feel sorry for him.')
        newline()
        if questaccept == 1:
            smartprint(
                'I will now be talking you throught your entire story. Great! There is no turning back. You will risk your life and most certainly lose prized limbs. You may take only one companion. Choose wisely from your choices.')
            companion = multiplechoice('Your friend (must be human)',
                                       'Llama',
                                       'Me',
                                       'The title of the army commander')
            if companion == 1:
                smartprint('What is this friend\'s name?')
                companion = 'your friend, ' + str(input('-> ')) + ','
                newline()
                smartprint('Hmm, I hope you trust this guy/girl!')
            elif companion == 2:
                companion = 'your llama'
                smartprint('Very wise, they are the wisest.')
            elif companion == 3:
                companion = 'me'
                smartprint('Welcome aboard myself!')
            elif companion == 4:
                companion = 'your army'
                smartprint('Smart choice, my entire army is at your command!')
            else:
                error()
            wait_key()
            newline()
            smartprint(
                'Your adventure begins! To get to the jelly you must first find out the destination. I do not know the precise location of this but I shall tell you what I know. The jelly is located at the palace of Jelly. This palace was originally located in the region of England, then it moved to a region where very few have gone. It is also the largest dessert you will ever have gone to on this Earth.')
            palacelocationtry = 0
            while True:
                palacelocation = multiplechoice('America',
                                                'Saudi Arabia',
                                                'Antarctica',
                                                'England')
                if palacelocation == 1:
                    smartprint(
                        'You tried, but it was dumb. Pleny have gone to America and America has hardly any desserts! But I shall give you another chance!')
                    palacelocationtry = 1
                elif palacelocation == 2:
                    smartprint('Interesting, it does have alot of dessert, but many have gone there. Try again.')
                    palacelocationtry = 1
                elif palacelocation == 3:
                    if palacelocationtry == 0:
                        smartprint(
                            'Correct! You are very wise and intelligent, you were the right man for the job by far!')
                    else:
                        smartprint('Took you more than one try, but still good job!')
                    break
                elif palacelocation == 4:
                    smartprint(
                        'You may be the dumbest person on the planet! I already told you it had been moved from England. You are definately not worthy. Goodybye. I shall have my army destroy you. Have a good day.')
                    theend()
                    break
                else:
                    error()
                    break
            wait_key()
            newline()
            smartprint(
                'You have traveled far distances to get to Antarctica with ' + companion + ' and found a dolphin friend but had to leave him behind. Very sad indeed. Now that you have arrived look at that view! Endless ice and white, and behind you is your ship, the blue sea and ' + companion + '!')
            wait_key()
            newline()
            smartprint('Look, in the distance their is a palace, wait two palaces? Wait let me think...')
            time.sleep(2)
            newline()
            if companion == 'your army':
                armysplit = ' Great! You can send half the army in each, which ever doesn\'t die a gruesome death will be the one to go into! Choose wisely!'
                smartprint(
                    'Oh! This is the trick in the legends, they built two indentical grand castles to trick some visitors into going into the one with traps and gruesome deaths.' + armysplit)
                palacechoice = multiplechoice('Sure, let them go!!',
                                              'Wow that\'s cruel, nah',
                                              'Can I just let one go in each?',
                                              'Don\'t feel like it.')
                if palacechoice == 1:
                    smartprint('I have ordered them to go! Lets wait and see the outcome...')
                    newline()
                    time.sleep(4)
                    smartprint(
                        'The other half of your army have died... I think I could hear their screaming from here! Anyway, lets go to the one who survived.')
                    companion = 'half of your army'
                elif palacechoice == 2:
                    smartprint(
                        'That was dumb, my army would be willing to sacrifice their lives for this jelly. Anyway, now its all their lives in your hands! Choose! ')
                    palacechoice = multiplechoice('The one to the left',
                                                  'The one to the right',
                                                  'Neither.',
                                                  'I can\'t choose!')
                    if palacechoice == 1 or palacechoice == 2 and random.randit(1, 2) == 1:
                        smartprint('Lucky! You didn\'t die! Congrats. Now for the hard part...')
                    elif palacechoice == 1 or palacechoice == 2 and random.randit(1, 2) == 2:
                        smartprint(
                            'Unlucky! You entered the wrong castle, I shall not describe the gruesome death you went through, but I think you can emagine...')
                    elif palacechoice == 3 or palacechoice == 4:
                        smartprint(
                            'Ok if you can\'t choose then let ' + companion + ' choose! Let\'s see what ' + companion + ' thinks...')
                        time.sleep(2)
                        newline()
                        if random.randint(1, 2) == 1:
                            palacechoice = 'left'
                        else:
                            palacechoice = 'right'
                        smartprint(
                            'I see that ' + companion + ' has chosen the ' + palacechoice + ' palace! Now go through and see if the choice was right.')
                        newline()
                        time.sleep(2)
                        if random.randint(1, 2) == 1:
                            smartprint('Lucky! You didn\'t die! Congrats. Now for the hard part...')
                        else:
                            smartprint(
                                'Unlucky! You entered the wrong castle, I shall not describe the gruesome death you went through, but I think you can emagine...')
                            time.sleep(1)
                            theend()
                    else:
                        error()
                elif palacechoice == 3:
                    smartprint(
                        'Wow! Your smarter than you think! That would give you more soldiers to use later. Ok lemme find two to send...')
                    time.sleep(1)
                    newline()
                    smartprint(
                        'Ok, found them. Lets wait and see how they go. Wow that was quick, one of them is already screaming. Great! Lets go to the one who survived.')
                elif palacechoice == 4:
                    smartprint(
                        'Did I just hear that? You are unworthy, how did you get to this point? No person shall ever insult a quest like that! You are left to eternal torture!')
                    theend()
                else:
                    error()
            else:
                armysplit = ' You must choose between them! Your choice is your fate! No pressure.'
                smartprint(
                    'Oh! This is the trick in the legends, they built two indentical grand castles to trick some visitors into going into the one with traps and gruesome deaths.' + armysplit)
                palacechoice = multiplechoice('The one to the left',
                                              'The one to the right',
                                              'Neither.',
                                              'I can\'t choose!')
                if palacechoice == 1 or palacechoice == 2 and random.randit(1, 2) == 1:
                    smartprint('Lucky! You didn\'t die! Congrats. Now for the hard part...')
                elif palacechoice == 1 or palacechoice == 2 and random.randit(1, 2) == 2:
                    smartprint(
                        'Unlucky! You entered the wrong castle, I shall not describe the gruesome death you went through, but I think you can emagine...')
                elif palacechoice == 3 or palacechoice == 4:
                    smartprint(
                        'Ok if you can\'t choose then let ' + companion + ' choose! Let\'s see what ' + companion + ' thinks...')
                    time.sleep(2)
                    newline()
                    if random.randint(1, 2) == 1:
                        palacechoice = 'left'
                    else:
                        palacechoice = 'right'
                    smartprint(
                        'I see that ' + companion + ' has chosen the ' + palacechoice + ' palace! Now go through and see if the choice was right.')
                    newline()
                    time.sleep(2)
                    if random.randint(1, 2) == 1:
                        smartprint('Lucky! You didn\'t die! Congrats. Now for the hard part...')
                    else:
                        smartprint(
                            'Unlucky! You entered the wrong castle, I shall not describe the gruesome death you went through, but I think you can emagine...')
                        time.sleep(1)
                        theend()
                else:
                    error()
            wait_key()
            newline()
            smartprint('Now after entering the castle you looked inside, shocked...')
            time.sleep(1)
            newline()
            smartprint(
                'It was made completely out of jelly, how had you not noticed? But that\'s not you problem. Your problem is the piece of jelly moving towards you, with eyes. You and ' + companion + ' prepare for the fight you know is coming. It, too, prepares. It gets it jelly sword, which looks flimsy, but no doubt lethal. How will you deal with this?')
            bossfight(companion)
        elif questaccept == 2:
            smartprint(
                'The homeless man replied, "Unwise, but it is your chioice. My existence is secret. To protect I shall have someone from my army to take care of you." The man dissapeared and was replaced by two knights. They both get their flame throwers out and set you on fire, then they leave. You are now know as a suicide bomber.')
            theend()
        elif questaccept == 3:
            smartprint(
                'The homeless man replied, "I see you are uncertain, too bad. You will not go in the quest. You must be willing and certain, too bad goodbye. I shall have to wipe your memory or kill you. If I wipe your memory you will become a homeless man on the streets known as Jed, like the person I have taken the form of temporary to see how wise you are. Good bye, you have 1 day to think. "')
            theend()
        elif questaccept == 4:
            smartprint(
                'The homeless man replied, "How could you! I am one of the most powerful people you will ever meet. You should be priveleged to be given this quest. This is an insult! I shall tell my master, who is even more powerful, your bad deeds. I shall deny the quest, you are not worth. Be ashamed. Goodbye." He three your coins at you and dissapeared in an instant. Than he was replaced by a person who looked like a knight. He said, "My master, the man you just met, has told me to take care of you. I am ordered to incinerate you. Please stay still for the process or I will have to make you. Thank you and have a great day. You were incinerated."')
            theend()
        else:
            error()
    elif wahtdoyousay == 4:
        smartprint('Nothing Happens, he disappears!')
    else:
        error()
    return


def run():
    while True:
        """A loop to let you restart the script"""
        start()
        newline()
        restartdragon = str(input('Do you want to restart? (y/n): '))
        if restartdragon == 'y':
            pass
        elif restartdragon == 'n':
            smartprint('Ending...')
            break
        else:
            smartprint('The answer is not "y" or "n". Assuming you want to quit.')
            smartprint('Ending...')
            break


if __name__ == '__main__':
    run()
