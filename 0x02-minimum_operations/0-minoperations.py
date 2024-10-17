#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0
    # Initialize operations count and current length
    ops = 0
    current = 1
    clipboard = 0

    while current < n:
        # If n is divisible by current, it's optimal to copy all and paste
        if n % current == 0:
            clipboard = current
            ops += 1  # Copy All operation
        
        # Paste operation
        current += clipboard
        ops += 1

    # If we've reached exactly n, return the operation count, else return 0
    return ops if current == n else 0
