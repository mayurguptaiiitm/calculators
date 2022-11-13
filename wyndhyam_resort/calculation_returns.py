occupancy_days=float(input("Enter the number of days you assume its full in an year: "))
# occupancy_days=328.5
# cost_of_property = float(input("Enter the amount invested for the property: "))
# cost_of_property = -431684.76
# print("Excel cost of property :" + str(cost_of_property))
print("Assuming the average rental rate is 341 USD, feel free to use variable to change this currently variable 'charge'")
print("Square meter of property set to default 106.365 m2 change using 'area' variable")
print("Invested amount is taken as 'invested' defaults to 294871 USD")
charge = 341
# area = 106.365 # before was 73
area = float(input("Enter area of flat: "))
invested = 294871
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
tax = -884.61
#final income
I = A + B + C + D + E + F + G + tax
#invested amount ROI
J = I/invested

print("Income after tax: " + str(A))
print("Marketing: " + str(B))
print("Reservation tour: " + str(C))
print("Cleaning laundry: " + str(D))
print("Hotelcommision: " + str(E))
print("Furniture change: " + str(F))
print("Resort maintainence: " + str(G))
print("Govt Tax: " + str(tax))
print("Final income: " + str(I))
print("ROI without loan: " + str(J*100))

EMI = 1976
print("Net profit per year = " + str(I - EMI*12))
print("Net profit per year (MXN)= " + str(20*(I - EMI*12)))
print("Net profit per month (MXN)= " + str((20*(I - EMI*12))/12))