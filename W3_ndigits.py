def ndigits(x):
    if abs(x) < 10:
        return 1
    if x == 0:
        return 0
    else:
        return 1+ndigits(x/10)
        

print ndigits(11111)