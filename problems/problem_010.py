"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from problem_007 import is_prime
import time


def summation_of_primes():
    total = 0
    value = 2
    while value < 2000000:
        if is_prime(value):
            total += value
        value += 1
    print total


if __name__ == "__main__":
    start_time = time.time()
    summation_of_primes()
    print "%s seconds" % (time.time() - start_time)
