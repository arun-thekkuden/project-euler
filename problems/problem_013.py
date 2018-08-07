# -*- coding: utf-8 -*-
u"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
File in problem_data/problem_013.txt
"""


def load_data():
    data = []
    with open('problem_data/problem_013.txt') as file:
        for line in file.readlines():
            data.append(long(line))
    return data


def calculate_first_10_digits(data):
    return str(sum(data))[0:10]


if __name__ == "__main__":
    data = load_data()
    print calculate_first_10_digits(data)
