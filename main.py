import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    print("Welcome to the Sandwich Maker")
    print("Available sandwiches: small, medium, large")
    print("What size of sandwich would you like to order? (q to quit)")
    size = input().strip().lower()

    while size != 'q':
        if size not in recipes:
            print("Invalid sandwich size. Please try again.")
        else:
            order_ingredients = recipes[size]['ingredients']
            cost = recipes[size]['cost']

            if sandwich_maker_instance.check_resources(order_ingredients):
                print(f"A {size} sandwich costs ${cost}. Please insert coins.")
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, cost):
                    if sandwich_maker_instance.make_sandwich(size, order_ingredients):
                        print("Enjoy your sandwich!")
                    else:
                        print("Error making sandwich. Please try again.")
                else:
                    print("Insufficient payment. Please try again.")
            else:
                print("Ingredients for this sandwich are not available. Please try again.")

        print("What size of sandwich would you like to order? (q to quit)")
        size = input().strip().lower()

    print("Thank you for using the Sandwich Maker.")


if __name__ == "__main__":
    main()
