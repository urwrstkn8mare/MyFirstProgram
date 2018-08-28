# PRG9


def AreaCalculator(shape, width, height, pivalue):
    global area
    pi = pivalue
    if shape == 'rectangle':
        area = width * height
    elif shape == 'triangle':
        area = (width * height) / 2
    elif shape == 'circle':
        area = (width * pi)
    else:
        print('You did not submit a shape to get the area of!')
        print('Ending!')
    return area


def run():
    while True:
        print('Welcome to Area Calculator!!')
        print('What shape would you like to find the area of? (triangle/rectangle/circle)')
        shapequery = input('-> ')
        print('')
        if shapequery == 'rectangle' or shapequery == 'Rectangle' or shapequery == 'triangle' or shapequery == 'Triangle':
            shapequery = shapequery.lower()
            print('What is the width of the ' + shapequery + '?')
            widthquery = int(input('-> '))
            print('')
            print('What is the height of the ' + shapequery + '?')
            heightquery = int(input('-> '))
            pivaluequery = 1
        elif shapequery == 'circle' or shapequery == 'Circle':
            shapequery = shapequery.lower()
            print('What is the diameter?')
            widthquery = int(input('-> '))
            print('')
            print('Would you like to input your own value of pi?')
            pivaluequery = str(input('-> '))
            print('')
            if pivaluequery == 'yes' or pivaluequery == 'y':
                print('Please input your pi value.')
                pivaluequery = int(input('-> '))
                print('')
            else:
                pivaluequery = 3.1415
            heightquery = 1
        else:
            print('You did not submit a shape to get the area of!')
            print('Ending!')
            break
        answer = AreaCalculator(shapequery, widthquery, heightquery, pivaluequery)
        print('The area of your ' + shapequery + ' is ' + str(answer) + '!')
        print('Bye!!')
        break


if __name__ == '__main__':
    run()
