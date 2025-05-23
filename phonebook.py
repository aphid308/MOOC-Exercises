class Person:
    def __init__(self, name):
        self.__name = name
        self.__numbers = []
        self.__address  = None
    def add_number(self, number):
        if len(number) > 0:
            self.__numbers.append(number)
        else:
            pass
    def add_address(self, address):
        if len(address) > 0:
            self.__address = address
        else:
            pass

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def __str__(self):
        return f"{self.name()}: {', '.join(self.numbers())}, {self.address()}"


class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            # add a new dictionary entry with an empty list for the numbers
            person = Person(name)
        person.add_number(number)
        self.__persons[name] = person
    def get_entry(self, name):
        return self.__persons[name]

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

    def get_name(self, number: str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        # self.__filehandler = FileHandler("phonebook.txt")
        #
        # # add the names and numbers from the file to the phone book
        # for name, numbers in self.__filehandler.load_file().items():
        #     for number in numbers:
        #         self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        entry = self.__phonebook.get_numbers(name)
        if entry is None:
            print("number unknown")
            return
        for number in entry.numbers():
            print(number)

    def search_number(self):
        number = input("number: ")
        name = self.__phonebook.get_name(number)
        if name == None:
            print("unknown number")
            return
        print(name)

    def exit(self):
        self.__filehandler.save_file((self.__phonebook.all_entries()))

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_number()
            else:
                self.help()

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                for number in numbers:
                    names[name] = number

        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")

if __name__ == "__main__":
    application = PhoneBookApplication()
    application.execute()