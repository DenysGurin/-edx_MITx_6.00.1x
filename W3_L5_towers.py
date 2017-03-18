steps = 0

def printMove(fr, to, n):
    print(' '*10*(5-n) + 'move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    global steps
    
    if n == 1:
        steps += 1
        #print steps
        #print (' '*10*(5-n) + 'level' + str(n))
        printMove(fr, to, n)
    else:
        #print (' '*10*(5-n) + 'level' + str(n))
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

Towers(20, 'a', 'b', 'c')
print steps