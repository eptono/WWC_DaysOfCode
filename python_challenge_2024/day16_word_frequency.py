#-------------------------------------------------------------------------------
# Day 16 Write a function that counts the frequency of each word in a sentence.
#
# Note: Upper- and lowercase occurences are treated as the same word.
#
#-------------------------------------------------------------------------------

import string

def get_word_list(s):
    '''Returns a list of the words in a given string after discarding
    punctuation. All words are transformed to lowercase.'''

    table = s.maketrans("", "", string.punctuation)
    return s.lower().translate(table).split()

def count_words():
    '''Asks the user to enter a sentence and returns a dictionary with the words
    from the string as keys and their frequency as values.'''

    s = input("Enter a sentence: ")
    lst = get_word_list(s)
    count_dict = {}

    for word in lst:
        count = lst.count(word)
        count_dict[word] = count

    return count_dict


print(count_words())


