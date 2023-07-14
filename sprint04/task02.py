order = 0


class Pizza:

    def __init__(self, products):
        global order
        self.ingredients = products
        order += 1
        self.order_number = order

    @staticmethod
    def hawaiian():
        return Pizza(["ham", "pineapple"])

    @staticmethod
    def meat_festival():
        return Pizza(["beef", "meatball", "bacon"])

    @staticmethod
    def garden_feast():
        return Pizza(["spinach", "olives", "mushroom"])