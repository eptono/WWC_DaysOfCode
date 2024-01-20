## Day 10: Write a program to remove duplicates from a list.
##
## Note: The order of the list elements will be maintained.
##------------------------------------------------------------------------------

def remove_duplicates(lst):
    unique_lst = []
    [unique_lst.append(x) for x in lst if x not in unique_lst]
    return """Original list: {lst}. List without duplicates: {unique}."""\
           .format(lst=lst, unique=unique_lst)

def main():

    lst1 = [2,3,5,3,6,4,2]
    lst2 = [12, 3*4, 12.0]
    lst3 = [(3*4==12), True]

    print(remove_duplicates(lst1))
    print(remove_duplicates(lst2))
    print(remove_duplicates(lst3))

if __name__ == '__main__':
    main()
