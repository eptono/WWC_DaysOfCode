#-------------------------------------------------------------------------------
# Day 17: Create a program that capitalizes the first letter of each word in a
# sentence.
#
#-------------------------------------------------------------------------------


def capitalize():

    string = str(input("Enter a string: "))
    return " ".join(word.capitalize() for word in string.split())

def main():
    print(capitalize())

if __name__ == '__main__':
    main()
