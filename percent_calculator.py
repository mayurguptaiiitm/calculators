initial_amount = input("Enter the initia amount :")
percentage = input("Enter the percentage :")
value = int(initial_amount)*int(percentage)/100
print(percentage + " of the amount  =" + str(value))
print("remaining amount " + str((int(initial_amount) - value)))
