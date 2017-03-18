s = 'azcbobobegghakl'

def count(s):
    total = 0 
    w = 0   
    for i in s:
        #print s[w:w+3], len(s[w:w+3])
        if s[w:w+3] == 'bob':
            total += 1
        w += 1
    return total
    
print count(s)