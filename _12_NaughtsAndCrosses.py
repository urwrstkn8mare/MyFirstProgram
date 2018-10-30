# Naughts and Crosses


def checkwin(box, player, turn):
    something = True

    def congrats():
        global something
        print('')
        print('-------------')
        print('| ' + box[1] + ' | ' + box[2] + ' | ' + box[3] + ' |')
        print('-------------')
        print('| ' + box[4] + ' | ' + box[5] + ' | ' + box[6] + ' |')
        print('-------------')
        print('| ' + box[7] + ' | ' + box[8] + ' | ' + box[9] + ' |')
        print('-------------')
        print('')
        print('Congrats ' + player[turn] + '! You have won. This is the end of this game, goodbye.')
        return False

    if box[1] == box[2] and box[3] == box[2]:
        something = congrats()
    elif box[4] == box[5] and box[6] == box[5]:
        something = congrats()
    elif box[7] == box[8] and box[9] == box[8]:
        something = congrats()
    elif box[1] == box[4] and box[4] == box[7]:
        something = congrats()
    elif box[2] == box[5] and box[5] == box[8]:
        something = congrats()
    elif box[3] == box[6] and box[6] == box[9]:
        something = congrats()
    elif box[1] == box[5] and box[5] == box[9]:
        something = congrats()
    elif box[7] == box[5] and box[5] == box[3]:
        something = congrats()
    else:
        pass
    return something


def instructions(playername):
    print('')
    print('Hello, ' + playername[1] + ' and ' + playername[2] + '. Welcome to naughts and crosses.')
    print('Players take turns to put their chosen symbol (either an X or an O) into the field in the grid.')
    print('Ready to start?')
    input()
    return


def game(playername):
    boxes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    playerturn = 1
    playerturnname = 'O'
    while True:
        print(playername[playerturn] + ', ' + playerturnname + ', please choose a place to choose.')
        print('-------------')
        print('| ' + boxes[1] + ' | ' + boxes[2] + ' | ' + boxes[3] + ' |')
        print('-------------')
        print('| ' + boxes[4] + ' | ' + boxes[5] + ' | ' + boxes[6] + ' |')
        print('-------------')
        print('| ' + boxes[7] + ' | ' + boxes[8] + ' | ' + boxes[9] + ' |')
        print('-------------')
        choiceinput = int(input('-> '))
        if 10 > choiceinput > 0:
            if boxes[choiceinput] == 'O' or boxes[choiceinput] == 'X':
                if boxes[1] in '1' or boxes[2] in '2' or boxes[3] in '3' or boxes[4] in '4' or boxes[5] in '5' \
                        or boxes[6] in '6' or boxes[7] in '7' or boxes[8] in '8' or boxes[9] in '9':
                    print('Sorry. This has already been taken. The turn is going to the other person.')
                    if playerturnname == 'O':
                        playerturnname = 'X'
                        playerturn = 2
                    elif playerturnname == 'X':
                        playerturnname = 'O'
                        playerturn = 1
                else:
                    print('Every box has filled. Game ended with none winning. :(')
                    print('Goodbye!')
                    break
            else:
                boxes[choiceinput] = playerturnname
                if checkwin(boxes, playername, playerturn):
                    pass
                else:
                    break
                if playerturnname == 'O':
                    playerturnname = 'X'
                    playerturn = 2
                elif playerturnname == 'X':
                    playerturnname = 'O'
                    playerturn = 1
                else:
                    print('Error. playerturnname error. Ending...')
                    break
            print('')
        else:
            print('Error. Incorrect input. Ending...')
            break
    return


def run():
    player = ['', 'player1', 'player2']
    print('What is player 1\'s name?')
    player[1] = str(input('-> '))
    print('What is player 2\'s name?')
    player[2] = str(input('-> '))
    instructions(player)
    game(player)


if __name__ == '__main__':
    run()
