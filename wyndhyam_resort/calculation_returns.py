from colorama import Fore,Back,Style

occupancy_days=float(input("Enter the number of days you assume its full in an year: "))
# occupancy_days=328.5
# cost_of_property = float(input("Enter the amount invested for the property: "))
# cost_of_property = -431684.76
# print("Excel cost of property :" + str(cost_of_property))
print("Assuming the average rental rate is 341 USD, feel free to use variable to change this currently variable 'charge'")
print("Square meter of property set to default 106.365 m2 change using 'area' variable")
print("Invested amount is taken as 'invested' defaults to 294871 USD")
# charge = 341
charge = float(input("Estimated average daily income: "))
# area = 106.365 # before was 73
area = float(input("Enter area of flat: "))
invested = float(input("Enter the amount invested in USD :"))
# invested = 294871
#Charge is then set to variable A as per documentation
A = charge*occupancy_days
print("income crude: " + str(A))
# calculating post IVA A
A = (A - (A*0.16))
# Getting in Marketing commision
B = A * -0.12
# Reservation charges and tour operations
C = A * -0.12
# cleaning and laundry per square meter
D = -12.7*area*12
# Hotel commission for their extraordinary work
E = (A + (B+C+D) )*-0.25
# Furniture change cost 
F = A * -0.05
#Resort maintainence 
G = 5 * area * -12
#Government Tax
tax = -float(input("Enter the govt Tax: "))
# tax = -884.61
#final income
I = A + B + C + D + E + F + G + tax
#invested amount ROI
J = I/invested

print(Back.GREEN + "Income after tax: " + str(A))
print(Back.RED +"Marketing: " + str(B))
print(Back.RED +"Reservation tour: " + str(C))
print(Back.RED +"Cleaning laundry: " + str(D))
print(Back.RED +"Hotelcommision: " + str(E))
print(Back.RED +"Furniture change: " + str(F))
print(Back.RED +"Resort maintainence: " + str(G))
print(Back.RED +"Govt Tax: " + str(tax))
print(Back.GREEN +"Final income: " + str(I))
print(Back.GREEN +"ROI without loan: " + str(J*100))
EMI = float(input("Enter your monthly EMI Here : "))
# EMI = 1976
print(Back.GREEN +"Net profit per year = " + str(I - EMI*12))
print(Back.GREEN +"Net profit per year (MXN)= " + str(20*(I - EMI*12)))
print(Back.GREEN +"Net profit per month (MXN)= " + str((20*(I - EMI*12))/12))
print(Back.RESET)