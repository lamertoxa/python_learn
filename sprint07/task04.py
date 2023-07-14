class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.methods_processing()
        self.rinsing.methods_processing()
        self.spinning.methods_processing()


class Washing:
    def wash(self):
        print("Washing...")

    def methods_processing(self):
        return self.wash()


class Rinsing:
    def rinse(self):
        print("Rinsing...")

    def methods_processing(self):
        return self.rinse()


class Spinning:
    def spin(self):
        print("Spinning...")

    def methods_processing(self):
        return self.spin()


if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()