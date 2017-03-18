from math import tan, pi
def polysum(n, s):
    area = (0.25*n*s**2)/tan(pi/n)
    perimeter = n*s
    return round(area + perimeter**2,4)