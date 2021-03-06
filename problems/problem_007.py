"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import sys
import time
from math import sqrt


def nth_prime_number(n):
    i = 3
    count = 2
    while count <= n:
        if is_prime(i):
            count += 1
        i += 1
    print i - 1


def is_prime(number):
    if number == 2:
        return True
    if number & 1 != 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    start_time = time.time()
    nth_prime_number(int(sys.argv[1]))
    print "%s seconds" % (time.time() - start_time)
