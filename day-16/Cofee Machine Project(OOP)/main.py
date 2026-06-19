from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
MENU = Menu()

machine_is_on = True

while machine_is_on:
    options = MENU.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        machine_is_on = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:   
        drink = MENU.find_drink(choice)
        if drink:
            if coffeemaker.is_resource_sufficient(drink):
                if moneymachine.make_payment(drink.cost):
                    coffeemaker.make_coffee(drink)
