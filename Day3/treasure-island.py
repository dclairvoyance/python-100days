print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("left or right? ").lower()
if (choice1 == "left"):
    choice2 = input("swim or wait? ").lower()
    if (choice2 == "wait"):
        choice3 = input("red or yellow or blue? ").lower()
        if (choice3 == "yellow"):
            print("You Win!")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
else:
    print("Game Over.")