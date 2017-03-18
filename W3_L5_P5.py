def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if b == 0 or a == 0:# or 
        print a,b
        return max(a,b)
    elif a > b:
        print a,b
        return gcdRecur(b, a % b)
    else:
        print a,b
        return gcdRecur(a, b % a)
        
print gcdRecur(18, 450)
print gcdRecur(180, 168)