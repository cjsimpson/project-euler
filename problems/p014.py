'''
Project Eurler Problem 14
http://projecteuler.net/problem=14
'''

sequence_cache = dict()

def create_sequence(seed):
    n = seed
    result = [n]
    while n > 1:
        if n in sequence_cache:
            result.extend(sequence_cache[n][1:])
            n = result[-1]
        else:
            if n % 2 == 0:
                n =  n / 2
            else:
                n = 3 * n + 1
            result.append(n)
            sequence_cache[seed] = tuple(result)
    return result
    
def find_longest_sequence(under_value):
        max_value = [0,0]   #Number, Sequence Length
        for x in xrange(under_value):
            seq_length = len(create_sequence(x))
            if seq_length > max_value[1]:
                max_value = [x,seq_length]
        return max_value[0]

if __name__ == '__main__':
    print find_longest_sequence(1000000)
