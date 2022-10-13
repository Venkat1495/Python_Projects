from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
# my_menuitem = MenuItem()
my_coffeemaker = CoffeeMaker()
my_moneymachine = MoneyMachine()


while True:
    user_req = input("What would you like? (espresso/latte/cappuccino): ").lower()

    is_true = True
    if user_req == "report":
        my_coffeemaker.report()
        my_moneymachine.report()
        continue
    elif user_req == "off":
        is_true = False
    if not is_true:
        break

    obj_menuitem = my_menu.find_drink(user_req)
    name = obj_menuitem.name
    cost = obj_menuitem.cost
    ingredents = obj_menuitem.ingredients

    if user_req == "espresso" or user_req == "latte" or user_req == "cappuccino" :
        is_true = my_coffeemaker.is_resource_sufficient(obj_menuitem)
        if not is_true:
            break

        is_true = my_moneymachine.make_payment(cost)
        if is_true:
            my_coffeemaker.make_coffee(obj_menuitem)
        elif not is_true:
            break


