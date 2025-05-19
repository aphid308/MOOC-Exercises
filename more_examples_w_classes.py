import math

class Point:
    """ The class represents a point in two-dimensional space """

    def __init__(self, x: float, y: float):
        # These attributes are public because any value is acceptable for x and y
        self.x = x
        self.y = y

    # This class method returns a new Point at origo (0, 0)
    # It is possible to return a new instance of the class from within the class
    @classmethod
    def origo(cls):
        return Point(0, 0)

    # This class method creates a new Point based on an existing Point
    # The original Point can be mirrored on either or both of the x and y axes
    # For example, the Point (1, 3) mirrored on the x-axis is (1, -3)
    @classmethod
    def mirrored(cls, point: "Point", mirror_x: bool, mirror_y: bool):
        x = point.x
        y = point.y
        if mirror_x:
            y = -y
        if mirror_y:
            x = -x

        return Point(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"


class Line:
    """ The class represents a line segment in two-dimensional space """

    def __init__(self, beginning: Point, end: Point):
        # These attributes are public because any two Points are acceptable
        self.beginning = beginning
        self.end = end

    # This method uses the Pythagorean theorem to calculate the length of the line segment
    def length(self):
        sum_of_squares = (self.end.x - self.beginning.x) ** 2 + (self.end.y - self.beginning.y) ** 2
        return math.sqrt(sum_of_squares)

    # This method returns the Point in the middle of the line segment
    def centre_point(self):
        centre_x = (self.beginning.x + self.end.x) / 2
        centre_y = (self.beginning.y + self.end.y) / 2
        return Point(centre_x, centre_y)

    def __str__(self):
        return f"{self.beginning} ... {self.end}"

class Student:
    """ This class models a student """

    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = ""):
        # calling the setter method for the name attribute
        self.name = name

        if len(student_number) < 5:
            raise ValueError("A student number should have at least five characters")

        self.__student_number = student_number

        # calling the setter method for the credits attribute
        self.credits = credits

        self.__notes = notes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name != "":
            self.__name = name
        else:
            raise ValueError("The name cannot be an empty string")

    @property
    def student_number(self):
        return self.__student_number

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, op):
        if op >= 0:
            self.__credits = op
        else:
            raise ValueError("The number of study credits cannot be below zero")

    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, notes):
        self.__notes = notes

    def summary(self):
        print(f"Student {self.__name} ({self.student_number}):")
        print(f"- credits: {self.__credits}")
        print(f"- notes: {self.notes}")

class Student:
    def __init__(self, name, completed_courses=[]):
        self.name = name
        self.completed_courses = completed_courses

    def add_course(self, course):
        self.completed_courses.append(course)

    # Adding completed courses to Sally's list also adds those courses to Sassy's list.
    # In fact, these two are the exact same list, as Python reuses the reference stored in the default value.
    # Creating the two new Student objects in the above example is equivalent to the following:
    # courses = []
    # student1 = Student("Sally Student", courses)
    # student2 = Student("Sassy Student", courses)
    ################################################
    # The default values of parameters should never be instances of more complicated, mutable data structures,
    # such as lists. The problem can be circumvented by making the following changes
    # to the constructor of the Student class:

class Student:
    def __init__(self, name, completed_courses=None):
        self.name = name
        if completed_courses is None:
            self.completed_courses = []
        else:
            self.completed_courses = completed_courses

    def add_course(self, course):
        self.completed_courses.append(course)

if __name__ == "__main__":
    point = Point(1, 3)
    print(point)

    origo = Point.origo()
    print(origo)

    point2 = Point.mirrored(point, True, True)
    print(point2)

    line = Line(point, point2)
    print(line.length())
    print(line.centre_point())
    print(line)

    # Passing only the name and the student number as arguments to the constructor
    student1 = Student("Sally Student", "12345")
    student1.summary()

    # Passing the name, the student number and the number of study credits
    student2 = Student("Sassy Student", "54321", 25)
    student2.summary()

    # Passing values for all the parameters
    student3 = Student("Saul Student", "99999", 140, "extra time in exam")
    student3.summary()

    # Passing a value for notes, but not for study credits
    # NB: the parameter must be named now that the arguments are not in order
    student4 = Student("Sandy Student", "98765", notes="absent in academic year 20-21")
    student4.summary()