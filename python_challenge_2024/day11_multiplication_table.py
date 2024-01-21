##Day 11: Write a program to print the multiplication table of a given number.
##
##This program randomly selects a number for creating a multiplication table.
##The maximum numbers to be multiplicated are 20 x 20.
##
##------------------------------------------------------------------------------

import random

def number_generator():
    num = random.randint(1, 20)
    return num

def calc_table(num):
    table = {}
    for i in range(1, 21):
        table[i] = i*num
    return table

def show_table():
    num = number_generator()
    table = calc_table(num)
    print("Multiplication table for {num}:".format(num=num))
    for multiplier in table:
        print(multiplier, "x", num, "=", table[multiplier])

def main():
    show_table()

if __name__ == '__main__':
    main()
