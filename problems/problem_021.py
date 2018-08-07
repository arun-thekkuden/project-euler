# -*- coding: utf-8 -*-
u"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def find_sum_divisors(number):
    factors_sum = 0
    for i in xrange(1, (number / 2) + 1):
        if number % i == 0:
            factors_sum += i
    return factors_sum


def calculate_sum_amicable(number):
    amicalble = []
    for a in xrange(1, number):
        b = find_sum_divisors(a)
        if a != b:
            c = find_sum_divisors(b)
            if c == a:
                if a not in amicalble:
                    amicalble.append(a)
                if b not in amicalble:
                    amicalble.append(b)
    return sum(amicalble)


if __name__ == "__main__":
    print calculate_sum_amicable(10000)
