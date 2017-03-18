def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    
    
    if exp > 0 and exp % 2 == 0:
        return recurPowerNew(base, exp/2) * recurPowerNew(base, exp/2)
    elif exp > 0 and exp % 2 != 0:
        return base * recurPowerNew(base, exp-1)
    else:
        return 1
        
print recurPowerNew(base=2, exp=5)