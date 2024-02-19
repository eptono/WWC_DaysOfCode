#-------------------------------------------------------------------------------
# Day 13: Write a program to shuffle the elements of a list randomly.
#-------------------------------------------------------------------------------


import random


def shuffle_game(lst):
    '''Shuffles and reshuffles the list as long as the user chooses so.'''

    while True:

        random.shuffle(lst)
        repeat = ask_repeat(lst)

        if repeat == "n":
            break


def ask_repeat(lst):
    '''Asks if the user wants to repeat shuffling.'''

    while True:

        repeat = input("Shuffled list: {lst}.\n\
        Shuffle again? y/n".format(lst=lst))

        if repeat == "y" or repeat == "n":
                break
        else:
            continue

    return repeat


def main():

    shuffle_game([0,1,2,3,4,5,6,7,8,9,10])


if __name__ == '__main__':
    main()
