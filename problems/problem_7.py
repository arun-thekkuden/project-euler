'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''

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
    print i-1


def is_prime(number):
    if number & 1 != 1:
        return False
    range_value = int(number/2) if sqrt(number) < 2 else int(sqrt(number))
    for i in range(2, int(number/2)):
        if number % i == 0:
            return False
    return True



# TODO - Not yet functional
def is_prime_project_euler_solution(number):
    if number == 1: 
        return False
    elif number < 4:
        return True
    elif number & 1 != 1:
        return False
    elif number < 9:
        return True
    elif number % 3 == 0:
        return False
    for i in range(5, int(sqrt(number)), 6):
        if number % i == 0:
            return False
        if number % (i+2) == 0:
            return False
    return True


if __name__ == "__main__":
    start_time = time.time()
    nth_prime_number(int(sys.argv[1]))
    print "%s seconds" % (time.time() - start_time)
