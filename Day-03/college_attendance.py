attendance=int(input("Enter your attendance:"))
medical=input('Do you have medical certificate(yes/no):').lower()
if attendance>=75:
    print("Eligible")
elif attendance<75 and medical=="yes":
    print("Eligible")
else:
    print("Not eligible") 
