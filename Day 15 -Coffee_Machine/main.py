from data import MENU
from data import resources

machine = True
money = 0


def espresso():
    global w
    global cost
    global m
    global c

    w = int(MENU["espresso"]["ingredients"]["water"])
    c = int(MENU["espresso"]["ingredients"]["coffee"])
    m = 0
    cost =float(MENU["espresso"]["cost"])


def latte():
    global w
    global cost
    global m
    global c

    w = int(MENU["latte"]["ingredients"]["water"])
    c = int(MENU["latte"]["ingredients"]["coffee"])
    m = int(MENU["latte"]["ingredients"]["milk"])
    cost = float(MENU["latte"]["cost"])


def cappuccino():
    global w
    global cost
    global m
    global c

    w = int(MENU["cappuccino"]["ingredients"]["water"])
    c = int(MENU["cappuccino"]["ingredients"]["coffee"])
    m = int(MENU["cappuccino"]["ingredients"]["milk"])
    cost = float(MENU["cappuccino"]["cost"])


def sufficient():
    global poop
    if resources['water'] < w:
        print('There is not enough water !! SORRY')
        poop = False
    elif resources['milk'] < m:
        print('There is not enough milk !! SORRY')
        poop = False
    elif resources['coffee'] < c:
        print('There is not enough coffee !! SORRY')
        poop = False


def coins():
    global cost
    global change
    print('Please insert coins')
    quarters = float(input ('How many quarters? : '))
    dimes = float(input ('How many dimes? : '))
    nickles = float(input('How many nickles? : '))
    penny = float(input('How many pennies? : '))

    mun = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (penny * 0.01)
    change = mun - float(cost)
    change = round(change,2)

while machine == True:
    run = False
    poop = True
    drink = input("What would you like to drink? (espresso/latte/cappuccino) (other commands 'report' and 'stop') ")
    if drink == "report":
        print (f"Water : {resources['water']}ml ")
        print (f"Milk : {resources['milk']}ml")
        print (f"Coffee : {resources['coffee']}g")
        print (f"Money : ${money}")
    elif drink == "stop":
        machine = False
        print("Goodbye")


    if drink == "espresso":
        espresso()
        coins()
        sufficient()
        if change >= 0 and poop == True:
            run = True
            print(f'Your change is ${change}')
            print('Here is your espresso !! Enjoy')
        elif change < 0 and poop == True:
            print("Sorry that's not enough. Money refunded")
    elif drink == "latte":
        latte()
        coins()
        sufficient()
        if change >= 0 and poop == True:
            run = True
            print(f'Your change is ${change}')
            print('Here is your latte !! Enjoy')
        elif change < 0 and poop == True:
            print("Sorry that's not enough. Money refunded")
    elif drink == "cappuccino":
        cappuccino()
        coins()
        sufficient()
        if change >= 0 and poop == True:
            run = True
            print(f'Your change is ${change}')
            print('Here is your cappuccino !! Enjoy')
        elif change < 0 and poop == True:
            print("Sorry that's not enough. Money refunded")

    if run == True:
        resources["water"] = int(resources["water"]) - w
        resources["milk"] = int(resources["milk"]) - m
        resources["coffee"] = int(resources["coffee"]) - c
        money += cost
