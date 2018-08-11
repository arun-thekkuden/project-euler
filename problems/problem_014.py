def find_longest_collatz(limit):
    max_len = 0
    number = 0
    for i in xrange(1, limit):
        collatz_len = collatz_length(i)
        collatz_length.cache.update({i: collatz_len})
        if max_len < collatz_len:
            max_len = collatz_len
            number = i
    return number


def collatz_length(number, length=0):
    if number in collatz_length.cache:
        return collatz_length.cache.get(number) + length
    if number == 1:
        return length + 1
    if number % 2 == 0:
        return collatz_length(number / 2, length=length + 1)
    return collatz_length(3 * number + 1, length=length + 1)


collatz_length.cache = {}


if __name__ == "__main__":
    print find_longest_collatz(1000000)
