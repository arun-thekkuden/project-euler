mapper = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'thousand',
}


def convert_number_to_words(number):
    if number < 0:
        raise ValueError

    if number <= 20:
        return mapper[number]

    if number > 20 and number < 100:
        if number % 10 == 0:
            return mapper[number]
        return mapper[int(number / 10) * 10] + ' ' + mapper[number % 10]

    if number < 1000:
        if number % 100 == 0:
            return mapper[number / 100] + ' ' + mapper[100]
        return mapper[number / 100] + ' ' + mapper[100] + ' and ' + convert_number_to_words(number % 100)
    if number < 1000000:
        if number % 1000 == 0:
            return convert_number_to_words(number / 1000) + ' ' + mapper[1000]
        return convert_number_to_words(number / 1000) + ' ' + mapper[1000] + ' ' + convert_number_to_words(number % 1000)


if __name__ == "__main__":
    print len("".join([convert_number_to_words(x).replace(' ', '') for x in xrange(1, 1001)]))
