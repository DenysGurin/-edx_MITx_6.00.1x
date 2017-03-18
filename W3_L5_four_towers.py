steps = 0

def printMove(fr, to, n):
    print(' '*10*(5-n) + 'move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare1, spare2):
    global steps
    
    if n == 1:
        steps += 1
        #print steps
        #print (' '*10*(5-n) + 'level' + str(n))
        printMove(fr, to, n)
    elif n < 1:
        pass
    else:
        #print (' '*10*(5-n) + 'level' + str(n))
        Towers(n-2, fr, spare1, spare2, to)
        Towers(1, fr, spare2, spare1, to)
        Towers(1, fr, to, spare1, spare2)
        Towers(1, spare2, to, fr, spare1)
        Towers(n-2, spare1, to, fr, spare2)

Towers(40, 'a', 'b', 's1', 's2')
print steps