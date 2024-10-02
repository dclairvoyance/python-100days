MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

money = 0.00
inserted = 0.00
sufficient = True

active = True

while active:
    choice = input("What would you like? (report/espresso/latte/cappuccino) ")
    while choice != "report" and choice != "off" \
        and choice != "espresso" and choice != "latte" and choice != "cappuccino":
        print("Invalid.")
        choice = input("What would you like? (report/espresso/latte/cappuccino) ")

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")
    elif choice == "off":
        active = False
    else:
        drink = MENU[choice]
        for ingredient in drink["ingredients"]:
            # resources not sufficient
            if resources[ingredient] < drink["ingredients"][ingredient]:
                print(f"Sorry, there is not enough {ingredient}.")
                sufficient = False
                break
        
        # resources sufficient
        if sufficient:
            print("Please insert coins.")
            for coin in COINS:
                while True:
                    try:
                        payment = int(input(f"How many {coin}? ")) * COINS[coin]
                        while payment < 0:
                            print("Invalid.")
                            payment = int(input(f"How many {coin}? ")) * COINS[coin]
                        inserted += payment
                        break
                    except ValueError:
                        print("Please enter int only.")
            
            # money not sufficient
            if inserted < drink["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            # money sufficient
            else:
                change = inserted - drink["cost"]
                money += drink["cost"]
                print(f"Here is ${change:.2f} in change.")
                for ingredient in drink["ingredients"]:
                    resources[ingredient] -= drink["ingredients"][ingredient]
                print(f"Here is your {choice}. Enjoy!")
            
            inserted = 0.00

print("Off.")