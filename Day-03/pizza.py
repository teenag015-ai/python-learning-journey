print("Welcome to Python Pizza!")

size = input("What size pizza do you want? S, M, L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# Size price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You have chosen an invalid size")
    exit()

# Pepperoni price
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra cheese price
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")
