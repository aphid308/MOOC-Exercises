class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons:
            return False
        else:
            return True

    def print_contents(self):
       print(f"There are {len(self.persons)} persons in this room,"
             f"and their combined height is {sum(p.height for p in self.persons)} cm")
       for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if not self.is_empty():
            sorted_persons = sorted(self.persons, key=lambda persons: persons.height)
            return sorted_persons[0].name
        else:
            return None

    def remove_shortest(self):
        if not self.is_empty():
            self.persons = sorted(self.persons, key=lambda persons: persons.height)
            return self.persons.pop(0)
        else:
            return None


if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()