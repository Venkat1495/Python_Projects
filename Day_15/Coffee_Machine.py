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


def report_off(rf):
    """Generate the report of current resources and also able to OFF the machine"""
    if rf == "report":
        print(f"Water: {resources['water']} \nMilk: {resources['milk']} \nCoffee: {resources['coffee']} \nMoney: {resources['money']}")
        return True
    elif rf == "off":
        return False


def re_check(user_bew):
    menu_choosie = MENU[user_bew]["ingredients"]
    if resources["water"] > menu_choosie["water"] :
        if resources["milk"] > menu_choosie["milk"] :
            if resources["coffee"] > menu_choosie["coffee"]:
                return True
            else:
                print("Sorry there is not enough coffee")
                return False
        else:
            print("Sorry there is not enough Milk")
            return False
    else:
        print("Sorry there is not enough Water")
        return False



def update_res(user_req):
    menu_choosie = MENU[user_req]["ingredients"]
    resources["water"] -= menu_choosie["water"]
    resources["milk"] -= menu_choosie["milk"]
    resources["coffee"] -= menu_choosie["coffee"]
    resources["money"] += MENU[user_req]["cost"]

# TODO 5. Process coins.
# TODO 6. Check transaction successful?


def coins(user_req):
    menu_choosie = MENU[user_req]
    qua = int(input("how many quarters?: "))
    dim = int(input("how many dimes?: "))
    nic = int(input("how many nickles?: "))
    pen = int(input("how many pennies?: "))
    total = (qua * 0.25) + (dim * 0.10) + (nic * 0.05) + (pen * 0.05)
    if total >= menu_choosie["cost"]:
        balance = total - menu_choosie["cost"]
        print(f"Here is {balance} in change.")
        update_res(user_req)
        print(f"Here is your {user_req} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while True:
    # TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    user_req = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 2. Turn off the Coffee Machine by entering "off”to the prompt.
    # TODO 3. Print report.
    resources["money"] = 0
    is_true = True
    if user_req == "report" or user_req == "off":
        is_true = report_off(user_req)
    if not is_true:
        break
    # TODO 4. Check resources sufficient?
    if user_req == "espresso" or user_req == "latte" or user_req == "cappuccino" :
        is_true = re_check(user_req)
        if not is_true:
            break
        is_true = coins(user_req)
        if not is_true:
            break



    # TODO 7. Make Coffee.
