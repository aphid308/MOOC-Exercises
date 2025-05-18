from datetime import date

person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}


def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:

    all_persons = {person1["name"]: person1, person2["name"]: person2, person3["name"]: person3}
    averages = {}

    for p in all_persons.values():
        average = p['result1'] + p['result2'] + p['result3']
        average = average / 3
        averages.update({p["name"]: average})
    min_key = min(averages, key=averages.get)

    return all_persons[min_key]

my_matrix = [[1, 2], [3, 4]]

def row_sums(my_matrix: list) -> list:
    for row in my_matrix[:]:
        row.append(sum(row))

date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

def list_years(dates: list) -> list:
    return [y.year for y in sorted(dates)]


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int) -> None:
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

# print(f"{python.author}: {python.name} ({python.year})")
# print(f"The genre of the book {everest.name} is {everest.genre}")

def older_book(book1: Book, book2: Book):
    if book1.year > book2.year:
        print(f"{book2.name} is older, it was published in {book2.year}.")
    elif book1.year < book2.year:
        print(f"{book1.name} is older, is was published in {book1.year}.")
    else:
        print(f"{book1.name} and {book2.name} were both published in {book2.year}.")

def books_of_genre(books: list, genre: str) -> list:
    return [b for b in books if b.genre == genre]

books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

print("Books in the crime genre:")
for book in books_of_genre(books, "crime"):
    print(f"{book.author}: {book.name}")
# older_book(python, everest)
# older_book(python, norma)

# class Pet:
#     def __init__(self, name: str, species: str, year_of_birth: int) -> None:
#         self.name = name
#         self.species = species
#         self.year_of_birth = year_of_birth
#
# def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
#     return Pet(name, species, year_of_birth)
#
# fluffy = new_pet("Fluffy", "dog", 2017)
# print(fluffy.name)
# print(fluffy.species)
# print(fluffy.year_of_birth)


