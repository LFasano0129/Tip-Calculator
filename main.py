# String to welcome the user
print("Welcome to the tip calculator")

# take input for the total cost of the bill and convert the variable to integer
total_bill = input("What was the total bill?\n")
total_bill_int = int(total_bill)

# loop to take input for tip percent and convert to correct float for the computation
tip_percent = input("What percentage of tip would you like to give? 10, 12, 15 or 20?\n")
tip_percent_int = int(tip_percent)

# take input for the total people who will split the bill and convert the variable to an integer
total_ppl = input("How many people will split the bill?\n")
total_ppl_int = int(total_ppl)

# calculate the total bill with tip
Bill_with_tip = tip_percent_int / 100 * total_bill_int + total_bill_int

# calculate the amount each person should pay
payment_per_person = Bill_with_tip / total_ppl_int

# f string to display the amount each person should pay
print(f"Each person should pay: {round(payment_per_person, 2)}")
