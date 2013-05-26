def proper_divisors(n):
    divisors = []
    if n > 1:
        divisors.append((1))
    for x in xrange(1, n-1 + 1):
        if n % x == 0 and x != 1:
            divisors.append(x)
    return divisors

def amicable_pairs_below(n):
    divisor_sums = {}
    for x in xrange(1, n):
        divisor_sums[x] = sum(proper_divisors(x))

    pairs = []
    skip_items = []
    for k,v in divisor_sums.iteritems():
        if k in skip_items:
            continue
        if v in divisor_sums:
            pairs.append(k)
            pairs.append(v)
            skip_items.append(k)
            skip_items.append(v)

    return sum(pairs)

def solve(n):
    return amicable_pairs_below(n)

if __name__ == '__main__':
    print solve(10000)