from datetime import datetime

class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name} (price {self.__price})"

    @property
    def price(self):
        return self.__price

    def __gt__(self, another_product):
        return self.price > another_product.price

    # Other Overloading Operators
    # < Less than __lt__(self, another)
    # > Greater than __gt__(self, another)
    # == Equal to __eq__(self, another)
    # != Not equal to __ne__(self, another)
    # <= Less than or equal to __le__(self, another)
    # >= Greater than or equal to __ge__(self, another)
    # + Addition __add__(self, another)
    # - Subtraction __sub__(self, another)
    # * Multiplication __mul__(self, another)
    # / Division (float) __truediv__(self, another)
    # // Division (integer) __floordiv__(self, another

class Note:
    def __init__(self, entry_date: datetime, entry: str):
        self.entry_date = entry_date
        self.entry = entry

    def __str__(self):
        return f"{self.entry_date}: {self.entry}"

    def __add__(self, another):
        # The date of the new note is the current time
        new_note = Note(datetime.now(), "")
        new_note.entry = self.entry + " and " + another.entry
        return new_note

#using repr and __str__ overloading
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"

    def __str__(self):
        return f"{self.name} ({self.age} years)"

if __name__ == "__main__":
    entry1 = Note(datetime(2016, 12, 17), "Remember to buy presents")
    entry2 = Note(datetime(2016, 12, 23), "Remember to get a tree")

    # These notes can be added together with the + operator
    # This calls the  __add__ method in the Note class
    both = entry1 + entry2
    print(both)