print("Welcome to treasure island")
print("Your mision is to find the treasure")
choice_1=input('You are in treasure land\n where do you want to go\n type "right" or "left"').lower()
if choice_1=="left":
    choice_2=input('you are in ocean\n do you want to swim or wait?\n type "swim" or "wait"').lower()
    if choice_2=="wait":
        choice_3=input('you are almost there!\n which door do you want?\n Red,Blue or Yellow:').lower()
        if choice_3=="yellow":
            print("You win the game")
        elif choice_3 =="red":
            print("Burned by fire Game Over")
        elif choice_3=="blue":
            print("Eaten by beasts .Game Over")
        else:
            print("Wrong door.Game Over")
        else:
        print("Attacked by tront Game Over")
    else:
        print("Fell into hole Game Over")


