class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}\n"

class Coffee(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"

class Chocolate(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50

    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"
class EmptyCup(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "empty cup"
        self.price = 0.90

    def description(self):
        return "An empty cup?! Gimme my money back!"
