##------------------------------------------------------------------------------
## Day 8: Write a function that accepts a string and calculates the number of
## uppercase and lowercase letters in it.
##
##------------------------------------------------------------------------------

def get_string():
    '''Returns the user input for a string.'''
    string = input(str("Enter some word(s): "))
    return string

def count_upper_lower(str):
    '''Returns the number of upper and lowercase characters in a string.'''
    upper = sum(1 for char in str if char.isupper())
    lower = sum(1 for char in str if char.islower())
    return upper, lower

def run_case_counter():
    '''Prompts the user for input until a string containing alphabetic
    characters is entered. Returns a message informing on the number of
    uppercase and lowercase characters in the string.'''
    while(True):
        str = get_string()
        upper, lower = count_upper_lower(str)
        if upper == 0 and lower == 0:
            print("There are no alphabetic characters in {str}.".
            format(str=str))
            continue
        else:
            output = """'{str}' contains {upper} uppercase and {lower} \
lowercase characters.""".format(str=str, upper=upper, lower=lower)
            break
    return output

def main():
    print(run_case_counter())

if __name__ == '__main__':
    main()
