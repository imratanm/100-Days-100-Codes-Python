print("welcome to the Tip Calculator!")

total_bill = float(input("Please enter the total bill amount: $"))
people = int(input("How many people are sharing the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_decimal = tip_percentage / 100
total_tip = total_bill * tip_decimal
total_bill_with_tip = total_bill + total_tip
bill_per_person = total_bill_with_tip / people
print(f"Each person should pay: ${bill_per_person:.2f}")   #formatted to 2 decimal places