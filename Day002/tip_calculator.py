print("Welcome to the tip calculator.")

while True:
    try:
        bill = float(input("What was the total bill? $"))
        break
    except ValueError:
        print("Please enter float only.")

while True:
    try:
        percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
        break
    except ValueError:
        print("Please enter int only.")

while True:
    try:
        people = int(input("How many people to split the bill? "))
        break
    except ValueError:
        print("Please enter int only.")

bill_per_person = "{:.2f}".format(round(bill * (100+percentage)/100 / people, 2))
print(f"Each person should pay: ${bill_per_person}")
print("Each person should pay: $%.2f" % round(bill * (100+percentage)/100 / people, 2))