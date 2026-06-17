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

profit = 0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def check_resources(drink):
    for i in MENU[drink]["ingredients"]:
       if MENU[drink]["ingredients"][i] > resources[i]:
           print(f"Sorry there is not enough {i}.")
           return False

    return True

def process_coins(quarters,dimes,nickles,pennies):
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money

def check_transaction(money,drink):
    if money < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = money - MENU[drink]["cost"]
        print(f"Here is ${change:.2f} in change.")
        return True

def make_coffee(drink):
    print(f"Here is your {drink}. Enjoy!")
    for i in MENU[drink]["ingredients"]:
        resources[i] = resources[i] - MENU[drink]["ingredients"][i]
                

machine_is_on = True

while machine_is_on:

    what = input("What would you like? (espresso/ latte/ cappuccino): ")

    if what == 'off':
        machine_is_on = False
    elif what == 'report':
        print_report()
    elif what not in MENU:
        print("Invalid drink choice.")
    else :
        if check_resources(what):
            print("Please insert coins.")
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickle = int(input("How many nickles?: "))
            penny =int(input("How many pennies?: "))
            
            money = process_coins(quarter,dime,nickle,penny)
            if check_transaction(money,what):
                make_coffee(what)
                profit += MENU[what]["cost"]
            

  




# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])
