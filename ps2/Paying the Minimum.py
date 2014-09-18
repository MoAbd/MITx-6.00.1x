n=1

monthalinterest=annualInterestRate/12
total=0
while n<13:
   
   
   monthlyPayment=monthlyPaymentRate*balance
   Monthlyunpaidbalance=balance-monthlyPayment
   interset=monthalinterest*Monthlyunpaidbalance
   
   
   balance =Monthlyunpaidbalance +interset
   total   =total +monthlyPayment
   
   print "Month: " ,n
   print "Minimum monthly payment:" ,round(monthlyPayment,2)
   print " Remaining balance:" , round(balance,2)
   
   n=n+1 
print"Total paid:" ,round(total,2)
print"Remaining balance:", round(balance,2)
