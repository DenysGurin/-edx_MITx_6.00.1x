balance = 3926
annualInterestRate = 0.2


def calculate_balance(balance, annualInterestRate):

    fixedMonthlyPayment = 0
    inputBalance = balance
    
    while balance >= 0:
        
        balance = inputBalance
        totalPaid = 0
        fixedMonthlyPayment += 10
        for mounth in range(1,13): 
          
            monthlyInterestRate = annualInterestRate / 12.0
            monthlyUnpaidBalance = balance - fixedMonthlyPayment
            balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
            totalPaid += fixedMonthlyPayment
                          
        
    
    print  'Lowest Payment: ' ,fixedMonthlyPayment   
    return 

calculate_balance(balance, annualInterestRate)