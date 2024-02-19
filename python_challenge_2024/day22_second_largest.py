#-------------------------------------------------------------------------------
# Day 22: Create a program to find the second-largest element in a list.
#
#-------------------------------------------------------------------------------


def second_largest(lst):
    '''Copies the given list but without its largest element. Then returns the
    largest element of that new list.'''

    lst = [item for item in lst if item != max(lst)]

    try:
        return max(lst)
    except Exception as e:
        return e

def main():

    l1 = [3,5,2,6,10,9,1,7,4,0,8]
    l2 = ['a', 'b', 'ac', 'aa', 'bbb', 'c']
    l3 = []

    print(second_largest(l1))
    print(second_largest(l2))
    print(second_largest(l3))

if __name__ == '__main__':
    main()
