# class Notebook:
#     """ A Notebook stores notes in string format """
#
#     def __init__(self):
#         # private attribute
#         self.__notes = []
#
#     def add_note(self, note):
#         self.__notes.append(note)
#
#     def retrieve_note(self, index):
#         return self.__notes[index]
#
#     def all_notes(self):
#         return ",".join(self.__notes)
#
# class NotebookPro(Notebook):
#     """ A better Notebook with search functionality """
#     def __init__(self):
#         # This is OK, the constructor is public despite the underscores
#         super().__init__()
#
#     # This causes an error
#     def find_notes(self, search_term):
#         found = []
#         # the attribute __notes is private
#         # the derived class can't access it directly
#         for note in self.__notes:
#             if search_term in note:
#                 found.append(note)
#
#         return found

class Notebook:
    """ A Notebook stores notes in string format """

    def __init__(self):
        # protected attribute
        self._notes = []

    def add_note(self, note):
        self._notes.append(note)

    def retrieve_note(self, index):
        return self._notes[index]

    def all_notes(self):
        return ",".join(self._notes)

class NotebookPro(Notebook):
    """ A better Notebook with search functionality """
    def __init__(self):
        # This is OK, the constructor is public despite the underscores
        super().__init__()

    # This works, the protected attribute is accessible to the derived class
    def find_notes(self, search_term):
        found = []
        for note in self._notes:
            if search_term in note:
                found.append(note)

        return found

class Person:
    def __init__(self, name: str):
        self._name = self._capitalize_initials(name)

    def _capitalize_initials(self, name):
        name_capitalized = []
        for n in name.split(" "):
            name_capitalized.append(n.capitalize())

        return " ".join(name_capitalized)

    def __repr__(self):
        return self.__name

class Footballer(Person):

    def __init__(self, name: str, nickname: str, position: str):
        super().__init__(name)
        # the method is available as it is protected in the base class
        self.__nickname = self._capitalize_initials(nickname)
        self.__position = position

    def __repr__(self):
        r =  f"Footballer - name: {self._name}, nickname: {self.__nickname}"
        r += f", position: {self.__position}"
        return r

# Test the classes
if __name__ == "__main__":
    jp = Footballer("peter pythons", "pyper", "forward")
    print(jp)