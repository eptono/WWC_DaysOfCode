#-------------------------------------------------------------------------------
# Day 33: Write a test case for a function that checks if a number is prime
#
# number.py: Code to be tested
# prime_test.py: Testing module
#
# This module tests the is_prime(self) method from class Number.
#
#-------------------------------------------------------------------------------

import unittest
import number


class TestPrime(unittest.TestCase):

    # Test cases for primes
    def test_primes(self):
        prime_lst = [2,3,5,7,11,13,17,19,23,29,37]
        tested = []
        for n in prime_lst:
            num = number.Number(n)
            self.assertEqual(num.is_prime(), True, "incorrect classification of {num}".format(num=num))
            tested.append(n)
        print("Tested primes: {lst}".format(lst = tested))


    # Test cases for non-primes
    def test_non_primes(self):
        num_lst = [1,4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30]
        tested = []
        for n in num_lst:
            num = number.Number(n)
            self.assertEqual(num.is_prime(), False, "incorrect classification of {num}".format(num=num))
            tested.append(n)
        print("Tested non-primes: {lst}".format(lst = tested))


# run tests

unittest.main()