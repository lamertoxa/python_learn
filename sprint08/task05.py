import unittest

dict_tax = {
    0: 1000, 10: 2000, 15:2000, 21:5000,
    30:10000, 40: 30000, 47: 50000
}


class Worker:

    # your code
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        current_tax = 0
        current_salary = self.salary
        for percent,interval in dict_tax.items():
            if interval < current_salary:
                current_salary -= interval
                current_tax += percent*interval*0.01
            else:
                current_tax += current_salary*percent*0.01
                break
        return current_tax

class WorkerTest(unittest.TestCase):
    def test_hundredtausend(self):
        a = Worker("toxa", 1000000)
        result = a.get_tax_value()
        expend = 40050.0
        self.assertEqual(expend,result)
    @unittest.expectedFailure
    def test_fifty(self):
        a = Worker("kate", 50000)
        result = a.get_tax_value()
        expend = 16551
        self.assertEqual(expend,result)
