import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
class Cart:
    def __init__(self, goods):
        self.goods = goods


    def get_total_price(self):
        discount = {5: 0.05, 7: 0.10, 10: 0.20}
        result = 0
        def counter (good):
            nonlocal result
            discount_price = 0
            for i in discount.keys():
                if 20 == good.count:
                    discount_price = 0.30
                    break
                elif i <= good.count:
                    discount_price = discount[i]

            return ((good.price - (good.price * discount_price)) * good.count)
        if isinstance(self.goods,tuple):
            for good in self.goods:
                result += counter(good)
        else:
            result +=counter(self.goods)
        return result


class CartTest(unittest.TestCase):
    def test_first(self):
        obj = Product("kate", 5, 4)
        mycart = Cart(obj)
        result = mycart.get_total_price()
        expected = 20
        self.assertEqual(expected, result)







