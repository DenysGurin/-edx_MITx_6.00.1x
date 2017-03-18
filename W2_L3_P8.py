x = 1234567
epsilon = 0.01
step = epsilon**2
num_guesses = 0
ans = 0.0
while (abs(abs(ans**2)-abs(x))) >= epsilon and abs(ans**2) <= abs(x):
    if x == 0:
        break
    else:
        ans += step
        num_guesses += 1
        
if x < 0:
    ans = -ans
    print ans
else:
    print ans
print num_guesses