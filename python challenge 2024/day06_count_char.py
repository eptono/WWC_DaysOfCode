## Day 6: Write a program to count the occurrences of a specific character in a
## string.
##
##
## This program asks the user to input a sequence and a character to search for
## in this sequence.
## If the sequence contains no alphabetic characters, the search result will be
## 0.
## No differentiation is made between uppercase and lowercase.
##------------------------------------------------------------------------------


def get_count_params():
    '''Returns the user input for a string and a character.
    The input string can be anything, but the character input runs in a loop
    until exactly one alphabetic character is entered.'''
    string = input(str("Enter some word(s): "))
    while(True):
        char = input(str("Enter one alphabetic character: "))
        if not char.isalpha() or len(char) != 1:
            continue
        else:
            break
    return string, char


def count(string, char):
    '''Returns the number of occurences of a character in a string.'''
    string = string.lower()
    char = char.lower()
    count = 0
    for element in string:
        if element == char:
            count += 1
    return count


def format_output(string, char, count):
    '''Returns a formatted output informing on the occurrences of a char
    in a string.'''
    times = "times"
    if count == 1:
        times = "time"
    return ("Character '{char}' occurs {count} {times} in '{string}'.".format
    (char=char, count=count, times=times, string=string))


def run():
    '''Calls char-in-string counting functionality and returns a formatted
    output with the user's input as basis.'''
    string, char = get_count_params()
    counter = count(string, char)
    return format_output(string, char, counter)


def main():
    print(run())


if __name__ == '__main__':
    main()
