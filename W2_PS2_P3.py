balance = 999999
annualInterestRate = 0.18

def calculate_balance(balance, annualInterestRate,\
fixedMonthlyPayment):

    totalPaid = 0
    mounthes = 12
    
    for mounth in range(1,13): 
        
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        totalPaid += fixedMonthlyPayment
        
        """print 'Mounth: ', mounth
        print 'Minimum monthly payment: ', round(fixedMonthlyPayment,2)
        print 'Remaining balance: ', round(balance,2)
        
        if mounth == mounthes:
            print 'Total paid: ', round(totalPaid,2)
            print 'Remaining balance: ', round(balance,2)"""
    
    return balance


def minMonthlyPayment(balance, annualInterestRate):

    inputBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    lower = balance/12
    upper = (balance*(1+monthlyInterestRate)**12)/12
    fixedMonthlyPayment = (lower + upper)/2.0
    tolerance = 0.01
    iteration = 0
    
    while abs(calculate_balance(balance, annualInterestRate,fixedMonthlyPayment)) >= tolerance:
        
        balance = inputBalance
        fixedMonthlyPayment = (lower + upper)/2.0
        
        if calculate_balance(balance, annualInterestRate,fixedMonthlyPayment) > 0:
            
            lower = fixedMonthlyPayment
        
        else:
            
            upper = fixedMonthlyPayment 
            
        iteration += 1       
        
    print 'Iterations: ',iteration                       
    print  'Lowest Payment: ' ,round(fixedMonthlyPayment,2)  
    return 

#calculate_balance(balance=1000, annualInterestRate=0.2,fixedMonthlyPayment=10)
minMonthlyPayment(balance, annualInterestRate)