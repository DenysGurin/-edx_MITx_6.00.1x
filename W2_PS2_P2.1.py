balance = 3329
annualInterestRate = 0.2
fixedMonthlyPayment = 300
def calculate_balance(balance, annualInterestRate,\
fixedMonthlyPayment):

    totalPaid = 0
    mounthes = 12
    
    for mounth in range(1,13): 
        
        monthlyInterestRate = annualInterestRate / 12.0
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        totalPaid += fixedMonthlyPayment
        
        print 'Mounth: ', mounth
        print 'Minimum monthly payment: ', round(fixedMonthlyPayment,2)
        print 'Remaining balance: ', round(balance,2)
        
        if mounth == mounthes:
            print 'Total paid: ', round(totalPaid,2)
            print 'Remaining balance: ', round(balance,2)
    return 

calculate_balance(balance, annualInterestRate,fixedMonthlyPayment)

