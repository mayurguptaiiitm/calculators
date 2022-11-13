principle_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest: "))
duration_loan = float(input("Enter the loan duration in years: "))
annual_profit = float(input("Enter the profit: ")) #29505.65

interest_rate = interest_rate/12
months = duration_loan*12
numerator = principle_amount*interest_rate/100*(1+(interest_rate/100))**months
denominator = (1+interest_rate/100)**months - 1
# print(numerator)
# print(denominator)
# EMI = (principle_amount*interest_rate/100*(1+(interest_rate/100))**months)/((1+(interest_rate/100)**months - 1))
EMI = numerator/denominator
print ("EMI effective monthly : " + str(EMI) + " USD")
print ("Annual Payment :" + str(12*EMI) + " USD")
print ("Effective earnings : " + str(annual_profit-12*EMI) +" USD")

print ("Annual Earnings MXN: " + str(20*(annual_profit-12*EMI)) +" MXN")
print ("Monthly Earnings in MXN : " + str((20*(annual_profit-12*EMI))/12)+" MXN")
