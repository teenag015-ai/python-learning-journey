bill=int(input("Enter the bill"))
people=int(input("enter the number of people"))
if bill>1000:
    tax=bill*10/100
    total_bill=bill+tax
    sharing=total_bill/people
    print(f"Amount each person should pay:{sharing} ")

else:
    sharing=bill/people
    print("Amount each person should pay",sharing)
