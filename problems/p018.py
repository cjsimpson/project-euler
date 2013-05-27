"""
Project Eurler Problem 18
http://projecteuler.net/problem=18
"""

def parse_input(data):
    output = []
    for line in data.strip().split('\n'):
        new_line = []
        for column in line.split():
            new_value = int(column)
            new_line.append(new_value)
        output.append(tuple(new_line))
    return output

def solve(data):
    triangle = parse_input(data)
    triangle.reverse()
    max_sums = list()

    for row_num, row in enumerate(triangle):
        previous_row = row_num - 1
        row_values = []

        if row_num == 0:
            max_sums.append(row)
            continue

        for col_num, col in enumerate(row):
            max_child = max(max_sums[previous_row][col_num], max_sums[previous_row][col_num + 1])
            row_values.append(col + max_child)

        max_sums.append(tuple(row_values))

    return max_sums[-1][0]


if __name__ == '__main__':
    data = """75
             95 64
            17 47 82
           18 35 87 10
            20 04 82 47 65
            19 01 23 75 03 34
            88 02 77 73 07 63 67
            99 65 04 28 06 16 70 92
            41 41 26 56 83 40 80 70 33
            41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
            70 11 33 28 77 73 17 78 39 68 17 57
            91 71 52 38 17 14 91 43 58 50 27 29 48
            63 66 04 68 89 53 67 30 73 16 69 87 40 31
            04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
            """

    print solve(data)