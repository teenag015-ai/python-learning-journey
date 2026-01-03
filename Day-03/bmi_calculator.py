height=int(input("enter your height:"))
weight=int(input("Enter your weight:"))
if weight<18.5:
    print("Underweight")
elif weight>=18.5 and weight<24.9:
    print("Normal")
else:
    print("Overweight")
