import random
from beverages import Coffee, Tea, Chocolate, Cappuccino, EmptyCup
class CoffeeMachine:
    class BrokenMachineException(Exception):
        def __init__(self, message="This coffee machine has to be repaired."):
            super().__init__(message)

    def __init__(self):
        self.is_broken = False
        self.drink_count = 0

    def repair(self):
        self.is_broken = False
        self.drink_count = 0

    def serve(self, drink_class):
        if self.is_broken:
            raise CoffeeMachine.BrokenMachineException()

        self.drink_count += 1
        if self.drink_count >= 10:
            self.is_broken = True
            self.drink_count = 0

        if random.choice([True, False]):
            return drink_class()
        else:
            return EmptyCup()

# Test the CoffeeMachine
if __name__ == '__main__':
    coffee_machine = CoffeeMachine()

    for _ in range(20):
        try:
            drink = coffee_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            if drink == False:
                print(f"Drink not found!: {drink}")    

            print(f"Served: {drink}")
        except CoffeeMachine.BrokenMachineException:
            print("The coffee machine is broken. Repairing...")
            coffee_machine.repair()

