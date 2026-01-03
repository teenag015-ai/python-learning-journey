days=int(input("Enter the number of days stayed"))
room=input('enter the room type(stanadard/delux)').lower()
if room=="standard":
    total_bill=days*1000
else:
    total_bill=days*2000
    print(f"Your bill is:{total_bill}")
    if days>3:
        discount=total_bill*10/100
        total_bill=total_bill-discount
        print(f "Your total bill is:{total_bill}")

