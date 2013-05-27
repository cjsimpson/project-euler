"""
Project Eurler Problem 67
http://projecteuler.net/problem=67

This problem is the same as Problem 18, only it uses a bigger data set
"""

from problems import p018

def solve():
    with open('data/p067.txt', 'r') as f:
        data = f.read()
        print p018.solve(data)

if __name__ == '__main__':
    solve()