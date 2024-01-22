## Day 12: Write a program to reverse a given string.
##
## This program takes a string from user input, turns it into a list and returns
## a joined string from the reversed list.
##------------------------------------------------------------------------------

def get_string():
    string = input(str("Enter something: "))
    return string

def reverse_string(string):
    lst = list(string)
    lst.reverse()
    return "".join(lst)

def show_reverse():
    string = get_string()
    if not string:
        output = "Empty string, nothing to reverse."
    else:
        reverse = reverse_string(string)
        output = "The reverse of {string} is {reverse}.".format(string=string,
                reverse=reverse)
    return output

def main():
    print(show_reverse())

if __name__ == '__main__':
    main()
