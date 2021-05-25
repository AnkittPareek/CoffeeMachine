from data import MENU
from data import resources

need = True
money = 0


def profit(coffee_type):
    global money
    money += MENU[coffee_type]["cost"]


def recal_res(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    if coffee_type == "espresso":
        return True
    else:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]


def report():
    global resources
    global MENU
    print(
        f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} g\nMoney: $ {money}')


def resource_check(water_req, milk_req, coffee_req):
    if water_req > resources["water"]:
        print("Sorry there is not enough water.")
    elif milk_req > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif coffee_req > resources["coffee"]:
        print("Sorry there is not enough coffee.")
    else:
        return True


def process_coins(coffee_type):
    quarters = int(input("How many quarters are you inserting?"))
    dimes = int(input("How many dimes are you inserting?"))
    nickels = int(input("How many nickels are you inserting?"))
    pennies = int(input("How many pennies are you inserting?"))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if coffee_type == "espresso":
        price = MENU["espresso"]["cost"]
    elif coffee_type == "latte":
        price = MENU["latte"]["cost"]
    elif coffee_type == "cappuccino":
        price = MENU["cappuccino"]["cost"]
    if price < total:
        print(f"here is your extra ${total - price}")
        profit(coffee_type)
        recal_res(coffee_type)
    elif price > total:
        print(f"You need to insert ${price - total} more. Money Refunded.")
    elif price == total:
        profit(coffee_type)
        recal_res(coffee_type)
    else:
        return True


def run():
    request = input("What would you like? (espresso/latte/cappuccino) : ")
    if request == "off":
        print("Shutting Down.....")
        global need
        need = False
    elif request == "report":
        report()
    elif request == "espresso":
        if resource_check(water_req=50, coffee_req=18, milk_req=0):
            process_coins("espresso")
    elif request == "latte":
        if resource_check(water_req=200, coffee_req=24, milk_req=150):
            process_coins("latte")
    elif request == "cappuccino":
        if resource_check(water_req=250, coffee_req=24, milk_req=100):
            process_coins("cappuccino")
    else:
        print("You have entered wrong choice please try again.")


while need:
    run()
