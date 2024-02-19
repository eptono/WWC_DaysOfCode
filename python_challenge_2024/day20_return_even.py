#-------------------------------------------------------------------------------
# Day 20: Write a function that takes a list of numbers and returns a new list
# containing only the even numbers.
#
#-------------------------------------------------------------------------------


def even_only(lst):

    try:
        return [item for item in lst if item%2==0]
    except Exception as e:
        return 'Non-numeric types in list: {e}'.format(e=e)


print(even_only([3,-2,5,7,4.6,2,10,0]))
print(even_only([]))
print(even_only(['bird', 'horse', 4, 5]))

