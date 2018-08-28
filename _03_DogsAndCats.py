def DogsAndCats():
    global ageNew
    name = input('What is your name?')
    name = str(name)
    print('')
    animal = input('Do you like Cats or Dogs?')
    animal = str(animal)
    print('')
    age = input('How old are you?')
    age = int(age)
    print('')
    if animal == 'dogs' or animal == 'Dogs' or animal == 'dog' or animal == 'Dog':
        ageNew = age * 7
    elif animal == 'cats' or animal == 'Cats' or animal == 'cat' or animal == 'Cat':
        ageNew = age * 12
    else:
        print('You did not choose an animal!')
        print('Do it again!')
        print('')
        DogsAndCats()
    print('Hello ' + name + '!')
    print('I know you are ' + str(age) + ' years old!')
    print('But since you like ' + str(animal) + ' you are ' + str(ageNew) + ' years in ' + str(animal) + ' age!')
    print('')
    return


def run():
    DogsAndCats()


if __name__ == '__main__':
    run()
