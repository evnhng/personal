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

# Initialize profit counter.
profit = 0



# TODO: Turn off the Coffee Machine by entering "off"



# TODO: Print report.

# if choice == 'report':
#     print('Water: ' + str(resources["water"]) + 'ml')
#     print('Milk: ' + str(resources["milk"]) + 'ml')
#     print('Coffee: ' + str(resources["coffee"]) + 'g')
#     print('Money: $' + str(round(profit,2)))


# TODO: Check resources sufficient?

# Takes the order ingredients as an argument. returns True if the machine has enough ingredients, returns False if not.
def resource_sufficient(order_ingreds):
    for item in order_ingreds:
        if order_ingreds[item] >= resources[item]:
           print(f"Sorry, there is not enough of {item}. ")
           return False
    return True

 
# TODO: Process coins.

def process_coins():
    print('Please insert coins. (quarters/dimes/nickels/pennies) ')
    #total = 0
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

# TODO: Check transaction successful?

# Takes the money received and drink costs as inputs. returns true if the money received is enough to cover the drink cost. returns false if not. 
def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2) # the change received is difference between payment and cost, round to 2 decimals.
        print(f'Your change is  ${change}.')
        global profit # profit variable is made global.
        profit += drink_cost # adds the drink cost to profit.
        return True
    else:
        print('Sorry, that is not enough money. Your money has been refunded.')
        return False


# TODO: Make Coffee.

def make_coffee(name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name}. Enjoy!")

# TODO: Prompt user by asking "What would you like?"

is_on = True

while is_on:
    choice = input(str("What would you like? (espresso/latte/cappuccino): ")).lower() # choices.
    if choice == 'off': # off case
        is_on = False
    elif choice == 'report': # report case
        print('Water: ' + str(resources["water"]) + 'ml')
        print('Milk: ' + str(resources["milk"]) + 'ml')
        print('Coffee: ' + str(resources["coffee"]) + 'g')
        print('Money: $' + str(round(profit,2)))
    else: # order case
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])


# TODO: Add functionality to refill ingredients in the machine. 
# TODO: Add functionality to withdraw money from machine. 