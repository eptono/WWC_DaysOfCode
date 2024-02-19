#-------------------------------------------------------------------------------
# Day 21: Create a program to remove a specific element from a set.
#
#-------------------------------------------------------------------------------

def remove_from_set(s, item):
    return {ele for ele in s if ele != item}

def main():

    s1 = {3, 4, 'b', True, False}

    print(remove_from_set(s1, 3))
    print(remove_from_set(s1, 1))
    print(remove_from_set(s1, 0))
    print(remove_from_set(s1, 'absent'))

if __name__ == '__main__':
    main()
