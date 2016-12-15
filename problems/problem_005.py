"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time


def number_generator():
    number = 20
    while True:
        yield number
        number += 20


def smallest_multiple():
    for i in number_generator():
        flag = True
        for j in range(1, 21):
            if i % j != 0:
                flag = False
                break
        if flag:
            break
    print i


if __name__ == "__main__":
    start_time = time.time()
    smallest_multiple()
    print "%s seconds" % (time.time() - start_time)
