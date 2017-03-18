s = 'azcbobobegghakl'

def count(s):
    total = 0     
    for i in range(len(s)):
        #print s[i:i+3]
        if s[i:i+3] == 'bob':
            total += 1
    return total
    
print count(s)