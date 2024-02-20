#-------------------------------------------------------------------------------
# Day 36: Write a Python program to check if two strings are anagrams
#
# Function are_anagrams(s1,s2) compares two lists of all alphabetic characters
# obtained from two given strings. Returns True if both character lists are
# equal.
#
#-------------------------------------------------------------------------------


def are_anagrams(string1, string2):
    '''Makes two lists of all alphabetic characters from both given strings,
    ignoring whitespace, upper-/lowercase and apostrophes. If one string is the
    anagram of the other, the sorted character lists will be identical.'''


    charlist1 = [string1[i].lower() for i in range(len(string1)) if string1[i].isalpha() == True]
    charlist2 = [string2[i].lower() for i in range(len(string2)) if string2[i].isalpha() == True]

    return sorted(charlist1) == sorted(charlist2)


def main():

    # Anagrams:
    print(are_anagrams("silent", "listen"))
    print(are_anagrams("dormitory", "dirty room"))
    print(are_anagrams("eleven plus two", "twelve plus one"))
    print(are_anagrams("the eyes", "they see"))
    print(are_anagrams("McDonald's restaurants", "Uncle Sam's standard rot"))

    # Not anagrams:
    print(are_anagrams("ansi", "siam"))


if __name__ == '__main__':
    main()
