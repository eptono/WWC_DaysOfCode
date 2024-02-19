#-------------------------------------------------------------------------------
# Day 23: Write a program that checks if a key exists in a dictionary.
#
#-------------------------------------------------------------------------------

# Option 1:
def check_key(some_dict, key):
    '''Returns True or False'''
    return key in some_dict.keys()


# Option 2:
def keycheck(some_dict, key):
    '''Returns a short message if {key} is in the dictionary.'''

    try:
        some_dict[key]
        return "{k} is a key".format(k=key)
    except:
        return "{k} is not a key".format(k=key)

def main():

    dict1 = {'a':'b', 'c':'d', 'e':'f'}

    print("Option 1:")
    print(check_key(dict1, 'a'))
    print(check_key(dict1, 'b'))

    print("Option 2:")
    print(keycheck(dict1, 'a'))
    print(keycheck(dict1, 'b'))


if __name__ == '__main__':
    main()
