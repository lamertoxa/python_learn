import abc
from abc import ABC, abstractmethod


class Goods:

    def __init__(self, price, discount_strategy=None):
        self.price = price
        self.discount_strategy = discount_strategy
        self.price_after_discount()

    def price_after_discount(self):
        if self.discount_strategy == None:
            return self.price
        return self.discount_strategy(self.price)

    def __repr__(self):
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"

def on_sale_discount(order):
    return order * 0.5


def twenty_percent_discount(order):
    return order * 0.8

print (Goods(20000, discount_strategy = twenty_percent_discount))


