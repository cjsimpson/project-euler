"""
Project Eurler Problem 15
http://projecteuler.net/problem=15
"""


def mid_point(length):
    if length == 0:
        return None
    if length == 1:
        return 0
    return length / 2


def calculate_pascal_row(row_num):
    if row_num == 0:
        return [1, ]
    pascal_row = []
    for x in xrange(row_num + 1):
        if x == 0:
            pascal_row.append(1)
            continue

        element = pascal_row[x - 1] * (row_num + 1 - x) / x
        pascal_row.append(element)
    return pascal_row


def solve(square_size):
    mid_points = []
    x = calculate_pascal_row(square_size * 2)
    return x[mid_point(len(x))]


if __name__ == '__main__':
    print solve(20)
