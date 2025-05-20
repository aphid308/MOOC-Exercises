class Person:

   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email

   def update_email_domain(self, new_domain: str):
       old_domain = self.email.split("@")[1]
       self.email = self.email.replace(old_domain, new_domain)


class Student(Person):

   def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
       self.credits = credits


class Teacher(Person):

   def __init__(self, name: str, email: str, room: str, teaching_years: int):
       self.name = name
       self.email = email
       self.room = room
       self.teaching_years = teaching_years



class Book:
   """ This class models a simple book """
   def __init__(self, name: str, author: str):
       self.name = name
       self.author = author

class Thesis(Book):
    """ This class models a graduate thesis """

    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade

class BookContainer:
   """ This class models a container for books """

   def __init__(self):
       self.books = []

   def add_book(self, book: Book):
       self.books.append(book)

   def list_books(self):
       for book in self.books:
           print(f"{book.name} ({book.author})")


class Bookshelf(BookContainer):
   """ This class models a shelf for books """

   def __init__(self):
       super().__init__()

   def add_book(self, book: Book, location: int):
       self.books.insert(location, book)

if __name__ == "__main__":
   # Create some books for testing
   b1 = Book("Old Man and the Sea", "Ernest Hemingway")
   b2 = Book("Silent Spring", "Rachel Carson")
   b3 = Book("Pride and Prejudice", "Jane Austen")

   # Create a BookContainer and add the books
   container = BookContainer()
   container.add_book(b1)
   container.add_book(b2)
   container.add_book(b3)

   # Create a Bookshelf and add the books (always to the beginning)
   shelf = Bookshelf()
   shelf.add_book(b1, 0)
   shelf.add_book(b2, 0)
   shelf.add_book(b3, 0)


   # Tulostetaan
   print("Container:")
   container.list_books()

   print()

   print("Shelf:")
   shelf.list_books()