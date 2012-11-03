'''
Project Eurler Problem 4
http://projecteuler.net/problem=4
'''

#TODO: This is too slow. Find a way to optimize

from p003 import find_prime_factors

def is_divisable_by_all_nums(list_of_numbers, dividend):
    for num in list_of_numbers:
        if dividend % num != 0:
            return False
    return True

def find_highest_factors(list_of_numbers):
    #TODO: This isn't very clean
    number_set = set(list_of_numbers)
    if 1 in number_set:
        number_set.remove(1)
    for x in list_of_numbers[::-1]:
        for y in list_of_numbers:
            if (x != 1 and y != 1 and x!=y) and (x % y == 0):
                try:
                    number_set.remove(y)
                except KeyError:
                    pass
    return number_set

def find_smallest_dividend(list_of_numbers):
    list_of_numbers = list(find_highest_factors(list_of_numbers))
    list_of_numbers.sort(reverse=True)
    print list_of_numbers
    lower_limit = max(list_of_numbers) * min(list_of_numbers)
    upper_limit = reduce(lambda x,y: x*y, list_of_numbers)
    
    print 'MIN %d' %  lower_limit
    print 'MAX %d' %  upper_limit
    
    for num in xrange(max(list_of_numbers), upper_limit):
        if is_divisable_by_all_nums(list_of_numbers, num):
            return num
            

print find_smallest_dividend(range(1,11))