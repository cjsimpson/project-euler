'''
Project Eurler Problem 17
http://projecteuler.net/problem=17

Solving by converting numbers to words and counting the characters

Could also try converting numbers to a number representing the number of
characters in that word instead, would be faster for very large numbers.
'''

NUMBER_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                70: 'seventy', 80: 'eighty', 90: 'ninety' , 0: ''
                }

SCALES = {2: 'hundred', 3: 'thousand', 6: 'million', 9: 'billion'} # Key represents number of zeros

def n_slice(data_to_slice, slice_size, right_to_left=False):
    sliced_data = []
    if right_to_left:
        data_to_slice.reverse()
        
    while len(data_to_slice) >= slice_size:
        sliced_data.append(data_to_slice[:slice_size])
        data_to_slice = data_to_slice[slice_size:]
    if len(data_to_slice):
        sliced_data.append(data_to_slice)
    
    if right_to_left:
        return [x[::-1] for x in sliced_data[::-1]]
    else:
        return sliced_data

def _two_digits_to_word(number):
    words = []
    if isinstance(number, list):
        number = ''.join([str(x) for x in number])
    lookup_key = int(number)
    if number == '00' or lookup_key == '0':
        return []
    if lookup_key > 20:
        lookup_key_digits = [int(digit) for digit in str(lookup_key)]
        lookup_key_ones = lookup_key_digits[-1]
        lookup_key_tens = lookup_key_digits[0] * 10
        words.append(NUMBER_WORDS[lookup_key_tens])
        words.append(NUMBER_WORDS[lookup_key_ones])
    else:
        # Everything under 20 already in NUMBER_WORDS dictionary
        words.append(NUMBER_WORDS[lookup_key])
    return words

def _three_digits_to_word(number):
    words = []
    words.append(NUMBER_WORDS[number[0]])
    if number[0] != 0:
        words.append(SCALES[2])
    two_digit_words = _two_digits_to_word(number[1:])
    if ''.join(two_digit_words) != '':
        words.append('and')
    words += two_digit_words
    return words

def number_to_word(number):
    digits = [int(digit) for digit in str(number)]
    words = []
    digit_chunks = n_slice(digits, 3, True)
    for pos, chunk in enumerate(digit_chunks):
        if len(chunk) != 3:
            words += _two_digits_to_word(chunk)
        else:
            words += _three_digits_to_word(chunk)
        if pos + 1 < len(digit_chunks):
            words.append(SCALES[3 * len(digit_chunks[pos + 1:])])
    if '' in words:
        words.remove('')
    return words

def solve():
    result = 0
    for num in xrange(1, 1001):
        words = number_to_word(num)
        words_no_spaces = ''.join(words)
        result += len(words_no_spaces)
    print result
    
if __name__ == '__main__':
    solve()
