def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    min_ab = min(a,b) 
    while not (a % min_ab == 0 and b % min_ab == 0):
        min_ab -= 1
    return min_ab

print gcdIter(a=3, b=15)