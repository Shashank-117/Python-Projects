from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while on == True:
    run = True
    p = menu.get_items()
    print(p)

    order = input('What would you like to drink? : ')
    if order == "report":
        money_machine.report()
        coffee_maker.report()
        run = False
    elif order == "stop":
        on = False
        run = False

    if run == True:
        drink = menu.find_drink(order)
        do = coffee_maker.is_resource_sufficient(drink)
        cost = drink.cost
        if do == True:
            mun = money_machine.make_payment(cost)
        if do == True and mun == True:
            coffee_maker.make_coffee(drink)


