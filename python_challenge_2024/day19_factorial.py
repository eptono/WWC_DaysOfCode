#-------------------------------------------------------------------------------
# Day 19: Write a function to calculate the factorial of a number.
#
#
#-------------------------------------------------------------------------------


import math


def calc_factorial(num):
    '''Returns the factorial of a given number, if defined.'''
    try:
        return math.factorial(num)
    except Exception as e:
        return e


def get_input():
    '''Returns an integer from user input.'''

    while(True):
        try:
            x = int(input("Enter an integer: "))
            break
        except:
            print("Faulty input")
    return x


def run_factorial():
    '''Returns the factorial of a number from user input.'''
    num = get_input()
    return calc_factorial(num)



print(calc_factorial(0))
print(calc_factorial(5))
print(calc_factorial(-5))
print(calc_factorial(5.0))

# Alternative:
run_factorial()


