# Made by Samit Shaikh
# To use, import file
# then use each function with its parameters as defined. 
# Please do not copy and paste the functions into your own code and not give me credit. 
# Thanks. The purpose of this code is to allow you to read, write and open txt files.


def openforwrite(path):
    return open(path, 'w+')


def write(var, string):
    var.write(string + '\n')
    return


def read(path, line):
    global content
    try:
        with open(path) as fr:
            content = fr.readlines()
            """to remove whitespace characters like `\n` at the end of each line"""
            content = [x.strip() for x in content]
    except FileNotFoundError:
        print('')
        error = 'ERROR! The file you gave was not found or there was a problem with the program. (the file must be in the same directory as this program.)'
        print(error)
        input()
        exit()
        raise
    if line == 0:
        content = content
    else:
        line = line - 1
        content = content[line]
    return content


def closeafterwrite(var):
    var.close()
    return
