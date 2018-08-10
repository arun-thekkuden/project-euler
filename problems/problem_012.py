# coding: utf-8
import math


def get_len_divisors(number):
    factors = get_prime_factors(number)
    return reduce(lambda x, y: x * y, map(lambda x: x + 1, factors.values()))


def get_prime_factors(number):
    factors = {2: 0}
    while number % 2 == 0:
        factors[2] += 1
        number = number / 2

    for i in xrange(3, int(math.sqrt(number)) + 1, 2):
        factors[i] = 0
        while number % i == 0:
            factors[i] += 1
            number = number / i
        if not factors[i]:
            factors.pop(i, None)
    if number > 2:
        factors[number] = 1
    return factors


def find_500_divisors():
    i = 1
    sum_ = 0
    while True:
        sum_ += i
        i += 1
        if get_len_divisors(sum_) >= 500:
            return sum_


if __name__ == "__main__":
    print find_500_divisors()
