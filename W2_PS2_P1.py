balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def calculate_balance(balance, annualInterestRate,\
monthlyPaymentRate):

    totalPaid = 0
    mounthes = 12
    
    for mounth in range(1,13): 
        
        monthlyInterestRate = annualInterestRate / 12.0
        minimumMonthlyPayment = monthlyPaymentRate * balance
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        totalPaid += minimumMonthlyPayment
        
        print 'Mounth: ', mounth
        print 'Minimum monthly payment: ', round(minimumMonthlyPayment,2)
        print 'Remaining balance: ', round(balance,2)
        
        if mounth == mounthes:
            print 'Total paid: ', round(totalPaid,2)
            print 'Remaining balance: ', round(balance,2)
    return 

calculate_balance(balance, annualInterestRate,monthlyPaymentRate)
