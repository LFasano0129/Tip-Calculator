# String to welcome the user
print("Welcome to the tip calculator")

# take input for the total cost of the bill and convert the variable to integer
total_bill = input("What was the total bill?\n")
total_bill_int = int(total_bill)

tip = 0

# loop to take input for tip percent and convert to correct float for the final computation
while tip == 0:
    tip_percent = input("What percentage of tip would you like to give? 10, 12, 15 or 20?\n")
    tip_percent_int = int(tip_percent)
    if tip_percent_int == 10:
        tip = 1.10
    elif tip_percent_int == 12:
        tip = 1.12
    elif tip_percent_int == 15:
        tip = 1.15
    elif tip_percent_int == 20:
        tip = 1.20
    else:
        print("Invalid tip amount, please retry")

# take input for the total people who will split the bill and convert the variable to an integer
total_ppl = input("How many people will split the bill?\n")
total_ppl_int = int(total_ppl)

# final computation to calculate what each person should pay and then display it to the user
payment_per_person = total_bill_int / total_ppl_int * tip
print(f"Each person should pay: {round(payment_per_person, 2)}")
