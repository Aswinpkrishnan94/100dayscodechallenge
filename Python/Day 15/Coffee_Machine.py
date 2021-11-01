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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True   # state variable

# Function to check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry. Not enough {item}\n")
            return False
        return True

# Function to process money
def process_coins():
    print("Please insert Money\n")
    total = float(input("How many Pounds?\n"))
    return total

# Function to check if transaction is successful
def is_successful(money_received, drink_cost):
    if money_received == drink_cost:
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough money")
        return False

# Function to dispense Coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Enjoy the coffee\n")

    is_on = True

# 1. To dispense 2. Turn off device 3. Report on Ingredients available
while is_on:
    choice = input("What would you lke to have? 1. Espresso 2. Latte 3. Cappuccino\n").lower()
    if choice == "power off":
        is_on = False
    elif choice == "report":
        print(f"{resources['water']} ml")
        print(f"{resources['milk']}ml")
        print(f"{resources['coffee']}g")
        print(f"Money ${'profit'}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



