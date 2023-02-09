import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} pound(s)")
        else:
            sandwich = recipes[choice]
            #     sandwich = {
            #     "ingredients": {
            #         "bread": 2,  ## slice
            #         "ham": 4,  ## slice
            #         "cheese": 4,  ## ounces
            #     },
            #     "cost": 1.75,
            # }
            if sandwich_maker.check_resources(sandwich["ingredients"]):
                payment = sandwich_maker.process_coins()
                if sandwich_maker.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker.make_sandwich(choice, sandwich["ingredients"])


if __name__ == "__main__":
    main()
