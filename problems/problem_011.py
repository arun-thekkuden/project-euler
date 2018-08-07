import numpy as np


def load_data():
    return np.loadtxt('problem_data/problem_011.txt', usecols=range(20))


def down(matrix, i, j):
    if i + 3 > 19:
        return 0
    return matrix[i][j] * matrix[i + 1][j] * matrix[i + 2][j] * matrix[i + 3][j]


def right(matrix, i, j):
    if j + 3 > 19:
        return 0
    return matrix[i][j] * matrix[i][j + 1] * matrix[i][j + 2] * matrix[i][j + 3]


def diagonal_right(matrix, i, j):
    if i + 3 > 19 or j + 3 > 19:
        return 0
    return matrix[i][j] * matrix[i + 1][j + 1] * matrix[i + 2][j + 2] * matrix[i + 3][j + 3]


def diagonal_left(matrix, i, j):
    if i + 3 > 19 or j - 3 < 0:
        return 0
    return matrix[i][j] * matrix[i + 1][j - 1] * matrix[i + 2][j - 2] * matrix[i + 3][j - 3]


def calculate_max_multiple(matrix):
    max_ = 0
    for i in xrange(0, 20):
        for j in xrange(0, 20):
            temp_max = max([down(matrix, i, j), right(matrix, i, j), diagonal_right(matrix, i, j), diagonal_left(matrix, i, j)])
            if temp_max > max_:
                max_ = temp_max
                last = (i, j, [down(matrix, i, j), right(matrix, i, j), diagonal_right(matrix, i, j), diagonal_left(matrix, i, j)])
            max_ = max_ if temp_max < max_ else temp_max
    print last
    return max_


if __name__ == "__main__":
    matrix = load_data()
    print calculate_max_multiple(matrix)
