def genPrimes():
    numb = 0
      
    while True:
        divisors = 0
        for div in range(1,numb+1):
            if numb%div == 0:
                divisors += 1
        if divisors == 2:
            next = numb
            yield next
        numb += 1
        
prime = genPrimes()
print range(1,1)
#for n in genPrimes():
    #print n
