# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
https://projecteuler.net/problem=4 .

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time


def is_pallindrome(number):
    return str(number) == str(number)[::-1]


def find_largest():
    max_value = 0

    for i in xrange(100, 999):
        for j in xrange(100, 999):
            current_value = i * j
            if is_pallindrome(current_value) and current_value > max_value:
                max_value = current_value
    print max_value


if __name__ == "__main__":
    start_time = time.time()
    find_largest()
    print "My program took", time.time() - start_time, "to run"
