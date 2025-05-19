class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def weight(self):
        if self.__items:
            return sum(i.weight() for i in self.__items)
        else:
            return 0

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)
        else:
            pass
    
    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")

    def heaviest_item(self):
        if self.__items:
            return max(self.__items, key=lambda item: item.weight())
        else:
            return None

    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        return f"{len(self.__items)} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def weight(self):
        if self.__suitcases:
            return sum(s.weight() for s in self.__suitcases)
        else:
            return 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
        else:
            pass

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        if len(self.__suitcases) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.weight()} kg"
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.weight()} kg"

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()






