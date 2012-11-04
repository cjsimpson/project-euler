'''
Project Eurler Problem 14
http://projecteuler.net/problem=14
'''

def sequence_generator(n):
    current_value = n
    result = [n]
    while current_value > 1:
        if current_value%2 == 0:
            current_value = current_value/2
        else:
            current_value = current_value*3 +1
        result.append(current_value)
    return result

def sequence_length(n):
    current_value = n
    length  = 1
    while current_value > 1:
        if current_value%2 == 0:
            current_value = current_value/2
        else:
            current_value = current_value*3 +1
        length += 1
    return length

def find_longest_sequence(under_value):
        max_value = [0,0]   #Number, Sequence Length
        for x in xrange(under_value):
            seq_length = sequence_length(x)
            if seq_length > max_value[1]:
                max_value = [x,seq_length]
        return max_value[0]

if __name__ == '__main__':
    print find_longest_sequence(1000000)