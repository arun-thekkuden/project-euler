# -*- coding: utf-8 -*-
u"""
The Fibonacci sequence is defined by the recurrence relation.

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

import sys
import math


def thousand_digit_fibonacci_number(max_digits):
    first, second, index = 1, 1, 2

    while True:
        new_number = first + second
        index += 1

        # The characteristic part of the log plus one gives the number of digits in the number (before the decimal)
        if int(math.log10(new_number)) + 1 == max_digits:
            print index
            break

        first, second = second, new_number


if __name__ == "__main__":
    thousand_digit_fibonacci_number(int(sys.argv[1]))
