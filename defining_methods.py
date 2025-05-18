
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.original_value = initial_value
        self.value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value <= 0:
            pass
        else:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.original_value


# counter = DecreasingCounter(55)
# counter.decrease()
# counter.decrease()
# counter.decrease()
# counter.decrease()
# counter.print_value()
# counter.reset_original_value()
# counter.print_value()

class BonusCard:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def add_bonus(self):
        # The variable bonus below is a local variable.
        # It is not a data attribute of the object.
        # It can not be accessed directly through the object.
        bonus = self.balance * 0.25
        self.balance += bonus

    def add_superbonus(self):
        # The superbonus variable is also a local variable.
        # Usually helper variables are local variables because
        # there is no need to access them from the other
        # methods in the class or directly through an object.
        superbonus = self.balance * 0.5
        self.balance += superbonus

    def __str__(self):
        return f"BonusCard(name={self.name}, balance={self.balance})"

class Person:
    def __init__(self, name: str):
        self.name = name
    def return_first_name(self):
        return self.name.split()[0]
    def return_last_name(self):
        return self.name.split()[1]

# peter = Person("Peter Pythons")
# print(peter.return_first_name())
# print(peter.return_last_name())
#
# paula = Person("Paula Pythonnen")
# print(paula.return_first_name())
# print(paula.return_last_name())

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.all_numbers = []

    def add_number(self, number:int):
        self.all_numbers.append(number)
        self.numbers += 1
        pass

    def count_numbers(self):
        return len(self.all_numbers)

    def get_sum(self):
        return sum(self.all_numbers)

    def average(self):
        if self.all_numbers:
            return self.get_sum() / self.count_numbers()
        else:
            return 0





