#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int) or n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor  # Each prime factor contributes its value to operations
            n = n // divisor
        divisor += 1
        
        # Optimization: if divisor^2 > n, then n is prime
        if divisor * divisor > n and n > 1:
            operations += n
            break
            
    return operations
