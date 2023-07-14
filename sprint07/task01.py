import abc
from abc import ABC ,abstractmethod
class Product(ABC):
    @abstractmethod
    def cook(self):
        """ Interface Method """

class FettuccineAlfredo:
    def __init__(self):
        self.name = "Fettuccine Alfredo"
    def cook(self):
        print(f"Italian main course prepared: {self.name}")

class Tiramisu:
    def __init__(self):
        self.name = "Tiramisu"
    def cook(self):
        print(f"Italian dessert prepared: {self.name}")
class DuckALOrange:
    def __init__(self):
        self.name = "Duck À L'Orange"
    def cook(self):
        print( f"French main course prepared: {self.name}")
class CremeBrulee:
    def __init__(self):
        self.name = "Crème brûlée"
    def cook(self):
        print(f"French dessert prepared: {self.name}")

class Factory:
    @abstractmethod
    def get_dish(self,type_of_meal):
        """ Interface Method """


class ItalianDishesFactory(Factory):
    def get_dish(self,type_of_meal):
        if type_of_meal =="main":
            return FettuccineAlfredo()
        if type_of_meal == "dessert":
            return Tiramisu()

class FrenchDishesFactory(Factory):
    def get_dish(self,type_of_meal):
        if type_of_meal =="main":
            return DuckALOrange()
        if type_of_meal == "dessert":
            return CremeBrulee()
class FactoryProducer:
    def get_factory(self,type_of_factory):
        if type_of_factory =="italian":
            return ItalianDishesFactory()
        if type_of_factory == "french":
            return FrenchDishesFactory()


fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()

