age = int(input("Enter your age: "))
show = input("Enter your show type (Morning/Afternoon/Night): ").lower()

bill = 0

if age < 12:
    bill = 100
elif age <= 60:
    bill = 150
else:
    bill = 120

# Night show extra charge
if show == "night":
    bill += 30

print(f"Your total bill is: {bill}")
