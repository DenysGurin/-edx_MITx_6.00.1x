x = 1234567
epsilon = 0.01
low = 0
high = x
ans = (high + low)/2.0
iterat = 0

while abs(ans**2-x) >= epsilon and iterat < 50:
    
    if abs(ans**2) > x:
        high = ans
    elif abs(ans**2) < x:  
        low = ans
    ans = (high + low)/2.0
    iterat += 1 
    
print ans
print iterat      