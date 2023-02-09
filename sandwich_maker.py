
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, quantity in ingredients.items():
            if ingredient not in self.machine_resources or self.machine_resources[ingredient] < quantity:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        if not self.check_resources(order_ingredients):
            return False
        for ingredient, quantity in order_ingredients.items():
            self.machine_resources[ingredient] -= quantity
        return True
