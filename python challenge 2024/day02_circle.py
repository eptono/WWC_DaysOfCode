## Day 2: Create a program to calculate the area of a circle given its radius.
##
## This program will ask the user to input a radius, then return the area of
## a circle with the chosen radius.
##
##------------------------------------------------------------------------------

import math

def get_user_input():
    return input("Please enter a radius: ")


def area_calc(radius):
    pi = math.pi
    return float(radius)*2*pi


def main():
    radius = get_user_input()
    area = area_calc(radius)
    print("The area of a circle with radius " + str(radius) + " is " + str(area) + ".")


if __name__ == '__main__':
    main()
