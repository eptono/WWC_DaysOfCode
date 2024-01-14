## Day 04: Find the sum of all elements in a list.
##
##------------------------------------------------------------------------------


def calc_sum(somelist):
    '''If the list contains other datatypes than int or float, an exception will be thrown.'''
    try:
        return sum(x for x in somelist)
    except:
        return "I don't know! :("

def show_sum(ls):
    '''If the list is empty, there will be no calculation.'''
    if ls:
        print("The sum of " + str(ls) + " is: " + str(calc_sum(ls)))
    else:
        print(str(ls) + ": Nothing to calculate")

def main():

    l1 = [1,2,3,4,5,6,7,8,9]
    l3 = [1, 2, -3]
    l2 = [1, 2/3, 3/4, -4.5, -5*6]
    l4 = []
    l5 = [1, 2.0, "three"]

    show_sum(l1)
    show_sum(l2)
    show_sum(l3)
    show_sum(l4)
    show_sum(l5)

if __name__ == '__main__':
    main()
