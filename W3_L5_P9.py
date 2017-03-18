def semordnilap(str1, str2):
    if (len(str1) == 1 and len(str2) == 1) and str1 == str2:
        return True
    elif str1[len(str1) - 1] == str2[0] and len(str1) == len(str2):
        return semordnilap(str1[ : -1], str2[1 :])
    else:
        return False
    
    

    
    
print semordnilap('gd', 'dog')