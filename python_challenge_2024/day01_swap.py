## Day 1: Create a program that swaps the values of two variables.
##
## This program will first ask the user to enter two arbitrary values to put
## in a box and drawer.
## After confirming the chosen contents of box and drawer,
## the items will be showcased again in reverse order.
##------------------------------------------------------------------------------

def get_user_input():
    """ Stores two values from user input prompts (any datatype is possible)."""
    box = (input("What's in the box? Enter one item (can be anything)."))
    drawer = (input("What's in the drawer? Enter another item."))
    return box, drawer

def swap(box, drawer):
    """ Returns the swapped values of the parameters """
    box, drawer = drawer, box
    return box, drawer

def main():
    box, drawer = get_user_input()
    new_box, new_drawer = swap(box, drawer)

    print("Swapped the contents of box and drawer!")
    print("Now this is in the box: " + new_box)
    print("And this is in the drawer: " + new_drawer)

if __name__ == '__main__':
    main()

