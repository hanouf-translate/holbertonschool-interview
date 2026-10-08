#!/usr/bin/python3
"""  Minimum Operations"""

def minOperations(n):
    """ method that calculates the fewest number of operations needed 
      to result in exactly n H characters in the file"""
    if n <= 1:
        return 0

    operations = 0
    d = 2

    while n > 1:
        while n % d == 0:
            operations += d
            n = n // d
        d += 1

    return operations

    
#if __name__ == "__main__":
#    n = 4
#    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

#    n = 12
#    print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) 

#    n = 13
#    print("Min # of operations to reach {} char: {}".format(n, minOperations(n))) 

        