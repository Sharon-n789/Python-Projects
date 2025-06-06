from menu import Menu
from Coffee_Machine.coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

working = "True"
while working:
    x = menu.get_items()
    choice = input(f"What would you like? {x}")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        working = "False"
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
