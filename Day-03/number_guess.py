user_no=input("Enter your user number:")
secret_no=input("enter your secret number:")
if user_no==secret_no:
    print("Correct")
elif user_no>secret_no:
    print("too high")
else:
    print("too Low")
