print("Welcome to Treasure Island. Your mission is to find the treasure.")

choice1 = input("left or right? ").lower()
while choice1 != "left" and choice1 != "right":
    print("Invalid.")
    choice1 = input("left or right? ").lower()

if (choice1 == "left"):
    choice2 = input("swim or wait? ").lower()
    while choice2 != "swim" and choice2 != "wait":
        print("Invalid.")
        choice2 = input("swim or wait? ").lower()

    if (choice2 == "wait"):
        choice3 = input("red or yellow or blue? ").lower()
        while choice3 != "red" and choice3 != "yellow" and choice3 != "blue":
            print("Invalid.")
            choice3 = input("red or yellow or blue? ").lower()
            
        if (choice3 == "yellow"):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")