monthlyPayment=0   
monthlyInterestRate = annualInterestRate/12


balanceCopy = balance
while balance > 0:
    balance = balanceCopy
    monthlyPayment += 10
    for i in range(12):
        monthlyUnpaid = balance - monthlyPayment
        balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid
print "Lowest Payment: "+str(round(monthlyPayment,2))
       
