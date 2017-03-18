def selSort(L):
    swap = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        n = 0
        print 'out while loop', L, n
        while j < len(L):
            print minVal, L[j]
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
            n += 1
            print 'while loop',L, n
        if minIndx != i:
            swap += 1
            print 'swap', swap
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    print L, n
    
def newSort(L):
    swap = 0
    for i in range(len(L) - 1):
        j=i+1
        n = 0
        print 'out while loop', L, n
        while j < len(L):
            print L[i], L[j]
            if L[i] > L[j]:
                swap += 1
                print 'swap', swap
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            n += 1
            print 'while loop',L, n  
    print L, n            
                
L = [5,8,2,9,3]
selSort(L)
print ""
L = [5,8,2,9,3]
newSort(L)