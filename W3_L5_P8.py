def isIn(char, aStr):
    
    if  aStr == '':
        return False
    else:
        start = 0
        end = len(aStr)
        middle = (start + end) / 2
        check = aStr[middle]
        print check, aStr, char
        
        if check == char and len(aStr) == 1:
            return True
        
        elif check > char and len(aStr) > 1:
            return isIn(char, aStr[start : middle])
        
        elif check < char and len(aStr) > 1:
            return isIn(char, aStr[middle : end])
            
        else:
            return False
    
    
print isIn('x', 'bbijv')