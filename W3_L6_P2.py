def oddTuples(aTup):
   
    newTup = ()
    i = 0
    while i <= len(aTup):
        
        newTup += (aTup[i],)
        i += 2
    
    return newTup

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))