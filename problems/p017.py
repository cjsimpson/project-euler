'''
Project Eurler Problem 17
http://projecteuler.net/problem=17
'''

NUMBER_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                12: 'twleve', 13: 'thirteen', 14: 'foruteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'ninteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
                70: 'seventy', 80: 'eighty', 90: 'ninety' 
                }
SCALES = {3: 'hundred', 4: 'thousand', 7: 'million', 10: 'billion'}

def number_to_word(number):
    digits = [int(digit) for digit in str(number)]
    print digits
    words = []
    for pos, digit in enumerate(digits):
        length = len(digits[pos:])
        if length >= 3:
            scale = SCALES[length]
            print scale
        
        # Less than 100
        else:
            lookup_key = digit
            if length == 2:
                lookup_key = lookup_key * 10   # Appends a zero
            if lookup_key == 0:
                continue   # Nothing to do for 0
            words.append(NUMBER_WORDS[lookup_key])
    return words

def solve():
    print ' '.join(number_to_word(208))

if __name__ == '__main__':
    solve()
