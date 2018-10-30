# Samit
#  Function to raise x to the power of y.


def x_power_y(x, y):
    if float(x).is_integer() and float(y).is_integer() and x > 0 and y > 0:
        # turns the x value into an integer
        x = int(x)
        # turns the y value into an integer
        y = int(y)
        # declares i as 1
        i = 1
        # declares newx as x
        newx = x
        # starts a loop as long as i is smaller than y
        while i < y:
            # makes newx equal to newx times x
            newx = newx * x
            # makes i equal to i plus 1
            i += 1
        # makes returnvar equal to newx
        returnvar = newx
    else:
        reason = ''
        if not float(x).is_integer():
            reason = reason + ' NOT WHOLE NUMBER'
        else:
            pass
        if not float(y).is_integer():
            reason = reason + ' NOT WHOLE NUMBER'
        else:
            pass
        if not x > 0:
            reason = reason + ' NOT ABOVE ZERO'
        else:
            pass
        if not y > 0:
            reason = reason + ' NOT ABOVE ZERO'
        else:
            pass
        if reason == '':
            reason = ' UNKNOWN'
        else:
            pass
        # if x and y is not a positive whole number
        # makes the variable error to string with the error message embedded
        error = '! ERROR ! >>> The two arguments (x=' + str(x) + ', y=' + str(
            y) + ') entered in function power() because:' + reason
        # makes returnvar equal to error
        returnvar = error
    # returns error
    return returnvar


def run():
    # mainline starts here

    # teachers test code
    print("My name is Samit Shaikh: ")
    print(x_power_y(-4, 16))
    print(x_power_y(1, 2))
    print(x_power_y(2, 1))
    print(x_power_y(2, 8))
    print(x_power_y(2, 64))
    print(x_power_y(3, 0))
    print(x_power_y(9.0, 2.0))
    print(x_power_y(25, 0.5))
    print(x_power_y(2.7, -3))
    print(x_power_y(-5, 3))

    # my test code
    print(x_power_y(2, 3))
    print(x_power_y(9, 3))
    print(x_power_y(5, 5))
    print(x_power_y(4, 4))
    print(x_power_y(4, 2))


if __name__ == '__main__':
    run()
