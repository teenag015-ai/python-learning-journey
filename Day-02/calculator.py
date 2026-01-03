print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10 15 20 "))
people = int(input("How many people to split the bill? "))

tip_percent = tip / 100
total_bill = bill * (1 + tip_percent)
each_person = total_bill / people
each_person = round(each_person, 2)

print(f"Each person should pay: {each_person}")
