#-------------------------------------------------------------------------------
# Day 33: Write a test case for a function that checks if a number is prime
#
# number.py: Code to be tested
# prime_test.py: Testing module
#
# This module defines class Number, which can successively be filled with
# various functionalities.
#
# Method is_prime(self) returns if a Number instance is a prime number.
#
#-------------------------------------------------------------------------------


from math import sqrt


class Number:

    def __init__(self, num):
        self.num = num

    def is_prime(self):

        n = self.num

        prime = False

        if n > 1:
            for i in range(2, int(sqrt(n) + 1)):
                if n%i == 0:
                    prime = False
                    break
            else:
                prime = True

        return prime


    # Placeholder for other number functionalities





