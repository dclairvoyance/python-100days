from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

active = True

while active:
    choice = input(f"What would you like? ({menu.get_items()}report) ")
    if choice != "off" and choice != "report":
        menu_item = menu.find_drink(choice)
        while menu_item == None and choice != "off" and choice != "report":
            print("Invalid.")
            choice = input(f"What would you like? ({menu.get_items()}report) ")
            if choice != "off" and choice != "report":
                menu_item = menu.find_drink(choice)
    
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        active = False
    else:        
        # resources sufficient
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)