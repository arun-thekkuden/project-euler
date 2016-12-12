# -*- coding: utf-8 -*-
u"""
The sum of the squares of the first ten natural numbers is.

    1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import sys


def sum_square_difference(limit):
    numbers = [i * i for i in range(1, limit + 1)]
    sum_of_squares = reduce(lambda a, b: a + b, numbers)
    square_of_sum = (limit * (limit + 1) / 2) ** 2
    print square_of_sum - sum_of_squares


if __name__ == "__main__":
    sum_square_difference(int(sys.argv[1]))
