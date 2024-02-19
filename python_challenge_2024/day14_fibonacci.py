#-------------------------------------------------------------------------------
# Day 14: Write a program to print the first n numbers of a Fibonacci sequence
#
# F(n) = F(n-1) + F(n-2)
# F(0) = 0
# F(1) = 1
#-------------------------------------------------------------------------------


def fib(n):

    fib_lst = [0, 1]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            num1 = fib_lst[i-1]
            num2 = fib_lst[i-2]
            fib_lst.append(num1 + num2)

        return fib_lst[-1]


# Option 1:
def fib_table(n):
    '''Returns a table of the first n numbers of a Fibonacci sequence'''

    for i in range(1, n+1):
        print("fib({i}) = {fib}".format(i=i, fib=fib(i)))


#Option 2:
def fib_lst(n):
    '''Returns the first n numbers of a Fibonacci sequence as a list'''

    return [fib(i) for i in range(1, n+1)]


def main():

    fib_table(10)
    print(fib_lst(10))


if __name__ == '__main__':
    main()
