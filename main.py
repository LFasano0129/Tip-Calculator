# String to welcome the user
print("Welcome to the tip calculator")

# take input for the total cost of the bill and convert the variable to integer
total_bill = input("What was the total bill? $")
total_bill_float = float(total_bill)

# loop to take input for tip percent and convert to correct float for the computation
tip_percent = input("What percentage of tip would you like to give? 10, 12, 15 or 20? ")
tip_percent_int = int(tip_percent)

# take input for the total people who will split the bill and convert the variable to an integer
total_ppl = input("How many people will split the bill? ")
total_ppl_int = int(total_ppl)

# calculate the total bill with tip
bill_with_tip = tip_percent_int / 100 * total_bill_float + total_bill_float

# calculate the amount each person should pay
bill_per_person = bill_with_tip / total_ppl_int

# round to two decimals
final_bill = "{:.2f}".format(bill_per_person)

# f string to display the amount each person should pay
print(f"Each person should pay ${final_bill}")
