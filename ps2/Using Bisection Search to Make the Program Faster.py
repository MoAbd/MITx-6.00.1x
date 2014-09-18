
monthlyPayment=0   
monthlyInterestRate = annualInterestRate/12.0

lower = balance / 12.0

upper  = (balance * (1 + monthlyInterestRate)**12) / 12.0 

balanceCopy = balance
while balance > 0.01 or balance <-0.01:
    balance = balanceCopy
    monthlyPayment = (lower+upper)/2.0
    for i in range(12):
        monthlyUnpaid = balance - monthlyPayment
        balance = monthlyUnpaid + monthlyInterestRate*monthlyUnpaid
    if balance>0:
        lower=monthlyPayment
    if balance <0 :
        upper=monthlyPayment
print "Lowest Payment: "+str(round(monthlyPayment,2))
