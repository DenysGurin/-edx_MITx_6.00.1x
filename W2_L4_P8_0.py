def finde_root(x = 9, power = 2, epsilon = 0.01):
    low = min(-1,x)
    high = max(1,x)
    root = (high + low)/2.0
    
    if x < 0 and power % 2 == 0:
        return None
        
    while abs(root**power - x) > epsilon:
        if root**power > x:
            high = root
        else:
            low = root
        root = (high + low)/2.0
        print low, high, root
    if power % 2 == 0:
        return root
    else:
        return root, -root

print ("answer is: " + str(finde_root(0.25,2, epsilon = 0.01)))