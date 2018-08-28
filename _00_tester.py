import sys, os, random
import string, csv


def wait_key():
    try:
        print('Press any key to continue!')
        result = None
        if os.name == 'nt':
            import msvcrt
            result = msvcrt.getch()
        else:
            import termios
            fd = sys.stdin.fileno()

            oldterm = termios.tcgetattr(fd)
            newattr = termios.tcgetattr(fd)
            newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
            termios.tcsetattr(fd, termios.TCSANOW, newattr)

            try:
                result = sys.stdin.read(1)
            except IOError:
                pass
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    except termios.error:
        try:
            print('Not correct device, instead...')
            input("Press enter to continue")
        except SyntaxError:
            pass
    return result


list = ['test1', 'test2']
print(list)
list.append('test3')
print(list)


def test():
    def test2():
        print('hello')

    test2()
    print('test')


test()


def importmodule(modulename):
    new_module = __import__(modulename)


testvar = 'Hello this is a test sentence!'
print(testvar)
testvar = len(testvar)
print(testvar)

testvar2 = 39
if testvar2 < 40:
    print('yes')
else:
    print('no')

print('Hi')

print(random.randint(1, 2))

myString = 'test123'
print(myString)
print(myString.find('t'))
print(myString[myString.find('t')])
print(myString.find('l'))
print(myString.find('tadfsest'))
print(myString[myString.find('tadfsest')])

myemail = '@domain.com'
newemail = myemail.split('@')
print(myemail)
print(newemail)

dictionary = {0: 'help',
              1: 'test',
              }

print(str(len(dictionary)))

teststringll = 'himynameissamit'
print(teststringll[0])
print(teststringll[1:])
email = 'check@check.com.au'
domain = email.split('@')[-1]
toplevel = domain.split('.')[1:]
print(domain)
print(toplevel)

testvar = 'hello my name is samit'
variable1 = testvar.split('a')
print(variable1)
print(str(len(variable1[2])))

tstvarr = ['lol']
# print(tstvarr[1])

tst = ['this', 'is', 'a', 'test', 'youshouldn\'tseethis']
print(tst)
print('-'.join(tst[1:2]))
tst.append('test2')
print(tst)
for i in range(len(tst)):
    print(tst[0])
results = []
with open('test.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
print(results)
listt = ['1', '2']
if type(listt) == type([]):
    print('ITS A LIST')
else:
    print('ITS NOT A LIST')


def run():
    pass


if __name__ == '__main__':
    run()
