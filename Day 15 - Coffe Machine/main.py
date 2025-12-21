from art import logo

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

def is_resource_sufficient(order_ingredients):
    '''
    Returns True when the order can be made, False if the ingredients are insufficient
    '''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print("Please enter coins: ")
    total = int(input("Enter how many quarter : ")) * 0.25
    total += int(input("Enter how many diems : ")) * 0.1
    total += int(input("Enter how many nickles : ")) * 0.05
    total += int(input("Enter how many pennies : ")) * 0.01

    return total


def is_transaction_successfull(money_received, drink_cost):
    '''Returns True when the payment is successfull, False if money is insufficient'''
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f"Here is your ${change} change.")
        return True
    else:
        print("Sorry thats not enouigh money. Money refunding.")
        return False
    
def make_coffe(drink_name , oredr_ingredients):
    '''
    Takes Drink name and order ingredients and make_coffe
    '''
    for item in oredr_ingredients:
        resources[item] -= oredr_ingredients[item]
    print(f"Here is your {drink_name}.")


profit = 0
is_on = True
print(logo)
while is_on:
    choice  = input("What whould you like ? (Espresso/Latte/Cappuccino).: ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml.")
        print(f"milk : {resources['milk']}ml.")
        print(f"coffee : {resources['coffee']}ml.")
        print(f"Money : ${profit}.")
    else:
        drink = MENU["choice"]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment , drink["cost"]):
                make_coffe(choice, drink["ingredients"])


        

