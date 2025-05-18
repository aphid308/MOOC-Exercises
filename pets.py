class Pet:
    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

class Person:
    def __init__(self, name: str, pet: Pet):
        self.name = name
        self.pet = pet

    def __str__(self):
        return f"{self.name}, whose pal is {self.pet.name}, is a {self.pet.breed}"

if __name__ == '__main__':
    hulda = Pet("Hulda", "mixed-breed dog")
    levi = Person("Levi", hulda)

    print(levi)