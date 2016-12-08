'''
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Completed on Thu, 8 Dec 2016, 16:17
'''

import sys


def sum_three_five(limit):
    sum = 0
    three_break = False
    five_break = False
    i = 1
    while not three_break or not five_break:
        multiple_of_three = 3 * i
        multiple_of_five = 5 * i
        if not three_break:
            if multiple_of_three >= limit: 
                three_break = True
            else:
                sum += multiple_of_three
        if not five_break and multiple_of_five % 3 != 0:
            if multiple_of_five >= limit:
                five_break = True
            else:
                sum += multiple_of_five
        i += 1
    print sum


def main():
    if len(sys.argv) < 2:
        print "Usage: python problem_1.py <integer>"
        return

    try:
        limit = int(sys.argv[1])
    except ValueError:
        print "Usage: python problem_1.py <integer>"
    else:
        sum_three_five(limit)


if __name__ == "__main__":
    main()
