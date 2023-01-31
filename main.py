### Data ###
# Andrew Overton

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources, recipes):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources
        self.recipes = recipes
        
        while True:
            # asks for user input
            self.user_input = str(input("What would you like? (small / medium / large / off / report) : "))
            
            # checks validity
            if self.user_input not in ["small", "medium", "large", "off", "report"]:
                print("Please choose a valid option.")
                continue
            
            # choices
            if self.user_input == "off": # A. if turn off the machine
                return
            elif self.user_input == "report": # B. show resource report
                self.report_resources()
                continue
            
            # C. process order
            ingredients = self.recipes[self.user_input]["ingredients"]
            # if not enough resources
            resource_available = self.check_resources(ingredients)
            if not resource_available: continue
            
            # get coin and cost 
            coins = self.process_coins()
            cost = self.recipes[self.user_input]["cost"]
            
             # check if sufficient coins
            transaction = self.transaction_result(coins, cost)
            if not transaction: continue
            
            self.make_sandwich(self.user_input, ingredients)
            print(f"{self.user_input} sandwich is ready. Bon appetit!")
            
    def report_resources(self):
        """prints amount of available resources"""
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} pound(s)")
    
    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        if self.machine_resources["bread"] < ingredients["bread"]:
            print("Sorry there is not enough bread.")
            return False
        if self.machine_resources["ham"] < ingredients["ham"]:
            print("Sorry there is not enough ham.")
            return False
        if self.machine_resources["cheese"] < ingredients["cheese"]:
            print("Sorry there is not enough cheese.")
            return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        
        while True:
            try:
                dollar_large = float(input("how many large dollars?: "))
                break
            except:
                print("Please enter numbers only.")
                continue

        while True:
            try:
                dollar_half = float(input("how many half dollars?: "))
                break
            except:
                print("Please enter numbers only.")
                continue
            
        while True:
            try:
                dollar_quarter = float(input("how many quarters?: "))
                break
            except:
                print("Please enter numbers only.")
                continue
            
        while True:
            try:
                dollar_nickel = float(input("how many nickels?: "))
                break
            except:
                print("Please enter numbers only.")
                continue
   
        total_dollar = (dollar_large) + (dollar_half*0.5) + (dollar_quarter*0.25) + (dollar_nickel*0.05)
        return total_dollar

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            print(f"Here is ${round(coins-cost, 4)} in change. ")
            return True
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
           
        ingredients = ["bread", "ham", "cheese"]
        for ingredient in ingredients:
            self.machine_resources[ingredient] -= order_ingredients[ingredient]
           

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources, recipes)

