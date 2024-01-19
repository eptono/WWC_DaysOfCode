##Day 9: Write a program to check if a number is even or odd.
##
##This program generates a random number and prints if it's even or odd.
##------------------------------------------------------------------------------

import random


def even_or_odd():
    number = random.randint(-2048, 2048)
    if number % 2 == 0:
        evenodd = "even"
    else:
        evenodd = "odd"
    return ("{number} is an {evenodd} number.".format
    (number=number, evenodd=evenodd))


def main():
    print(even_or_odd())

if __name__ == '__main__':
    main()
