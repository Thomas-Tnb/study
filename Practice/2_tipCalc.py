# Tip Calculator 
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give ? $"))
people = int(input("How many people to split the bills? $"))

print(f"Each person should pay ${(total_bill + tip) / people}")

