## Day 3: Write a function to count the number of vowels in a given string.
##
## Wannado in the future: include vowels from other languages than English.

def get_string():
    '''Casting to string type allows any alphanumeric input.'''
    words = input("Please enter some words: ")
    return str(words)

def count_vowels(seq):
    vowels = ["a", "e", "i", "o", "u"]
    seq = seq.lower()
    count = 0
    for token in seq:
        if token in vowels:
            count += 1
    return count

def main():
    sequence = get_string()
    vowel_count = count_vowels(sequence)
    if vowel_count == 1:
        print("There is " + str(vowel_count) + " vowel in '" + sequence + "'.")
    else:
        print("There are " + str(vowel_count) + " vowels in '" + sequence + "'.")

if __name__ == '__main__':
    main()
