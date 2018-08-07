def load_data_into_array():
    with open('problem_data/problem_022.txt') as file:
        for line in file:
            data = line.replace('"', '').split(",")
    return sorted(data)


def calculate_total_score(data):
    total_score = 0
    for index, item in enumerate(data, 1):
        total_score += (sum([ord(char) - 96 for char in item.lower()]) * index)
    return total_score


if __name__ == "__main__":
    data = load_data_into_array()
    print calculate_total_score(data)
