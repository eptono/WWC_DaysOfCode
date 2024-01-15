##Write a program to find the maximum and minimum values in a list.
##
##------------------------------------------------------------------------------


def calc_min_max(lst):
    return min(lst), max(lst)


def minmax(lst):
    '''Depending on the list, returns a) min/max, b) exception message,\
       c) info on empty list.'''
    if lst:
        try:
            mini, maxi = calc_min_max(lst)
            output = format_output(lst, mini, maxi)
        except Exception as e:
            output = "That didn't work: {}".format(e)
    else:
        output = "Empty list: nothing to compare"

    return output


def format_output(lst, mini, maxi):
    return "{lst}: min is {mini}, max is {maxi}".format(lst=lst, mini=mini,\
    maxi=maxi)


def main():

    print(minmax([2,3,0,-19.7]))
    print(minmax(["you", "I", "we"]))
    print(minmax([1]))
    print(minmax([]))
    print(minmax([1, 2, "three"]))


if __name__ == '__main__':
    main()
