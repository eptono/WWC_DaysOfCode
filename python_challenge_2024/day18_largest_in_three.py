#-------------------------------------------------------------------------------
# Day 18: Create a program to find the largest among three numbers.
#
# This program asks the user to input three integers, then returns the largest
# of the three entered numbers.
#-------------------------------------------------------------------------------

def largest_of_three():

    num_lst = []

    for i in range(1, 4):
        while(True):
            try:
                x = int(input('Enter integer {i}: '.format(i=i)))
                num_lst.append(x)
                break
            except:
                print("Faulty input")

    return max(num_lst)


def main():

    print(largest_of_three())


if __name__ == '__main__':
    main()
