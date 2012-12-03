'''
Project Eurler Problem 6
http://projecteuler.net/problem=6
'''


def find_sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)


def find_square_of_sums(numbers):
    return sum(numbers) ** 2

if __name__ == '__main__':
    r = range(1, 101)
    result = find_square_of_sums(r) - find_sum_of_squares(r)
    print result
