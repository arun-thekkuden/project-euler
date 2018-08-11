def find_pythagorean_triplet():
    for i in xrange(1, 999):
        for j in xrange(i + 1, 1000):
            k = 1000 - i - j
            if i**2 + j**2 - k**2 == 0:
                return i * j * k


if __name__ == "__main__":
    print find_pythagorean_triplet()
