## Day 7: Write a program to check if a number is positive, 0 or negative.
##
## This program takes a number entered by the user and informs if the number is
## positive, zero or negative. Mathematical operations will not be parsed into
## valid input.
##
##------------------------------------------------------------------------------

def get_number():
    '''Returns a number (cast to float) from user input.'''
    while(True):
        try:
            number = float(input("Enter a number: "))
            break
        except Exception as e:
            print(e)
    return number


def analyse_number():
    '''Returns a message on which number range the chosen number falls into.'''
    number = get_number()
    signum = 0
    if number != 0:
        if number > 0:
            signum = "positive"
        else:
            signum = "negative"
    return "{number} is {signum}.".format(number=str(number),
    signum=str(signum))#format_output(number, signum)


def main():

    print(analyse_number())


if __name__ == '__main__':
    main()
