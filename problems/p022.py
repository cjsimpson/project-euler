"""
Project Eurler Problem 22
http://projecteuler.net/problem=22
"""

def parse_names(raw_names):
    return raw_names.replace('"', '').split(',')


def solve(names):
    names.sort()
    result = 0
    for pos, name in enumerate(names):
        name_letter_numbers = []
        for char in name.upper():
            name_letter_numbers.append(ord(char) - 64)
        result += sum(name_letter_numbers) * (pos + 1)
    return result

if __name__ == '__main__':
    with open('data/p022.txt', 'r') as f:
        names = parse_names(f.read())
        print solve(names)