class CourseRecord:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits

    def name(self):
        return self.__name
    def grade(self):
        return self.__grade
    def credits(self):
        return self.__credits
    def __gt__(self, other):
        return self.grade() > other.grade()
    def __lt__(self, other):
        return self.grade() < other.grade()
    def __eq__(self, other):
        return self.grade() == other.grade()
    def __str__(self):
        return f"{self.name()} ({self.credits()} cr) grade {self.grade()}"

class GradeBook:
    def __init__(self):
        self.__courses = {}

    def add_course(self, course: CourseRecord):
        course = course
        if course.name() not in self.__courses:
            self.__courses[course.name()] = course
        else:
            if course > self.__courses[course.name()]:
                self.__courses[course.name()] = course
            else:
                pass

    def get_course(self, name:str):
        if name in self.__courses:
            return self.__courses[name]
        else:
            return None

    def total_courses(self):
        return len(self.__courses)

    def total_credits(self):
        total = 0
        for course in self.__courses.values():
            total += course.credits()
        return total

    def gpa(self):
        grade_list = []
        for course in self.__courses.values():
            grade_list.append(float(course.grade()))
        return sum(grade_list) / len(grade_list)

    def distribution(self):
        grades = []
        grade_distribution = {}
        for course in self.__courses.values():
            grades.append(course.grade())
        for g in [5, 4, 3, 2, 1]:
            grade_distribution[g] = grades.count(g)
        return grade_distribution

class CourseRecordApplication:
    def __init__(self):
        self.gradebook = GradeBook()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_entry(self):
        course = input("course: ")
        grade = input("grade: ")
        credits = input("credits: ")
        record = CourseRecord(course, int(grade), int(credits))
        self.gradebook.add_course(record)

    def get_entry(self):
        name = input("name: ")
        if self.gradebook.get_course(name) is None:
            print("no entry for this course")
        else:
            print(self.gradebook.get_course(name))

    def get_statistics(self):
        total_courses = self.gradebook.total_courses()
        total_credits = self.gradebook.total_credits()
        grade_distribution = self.gradebook.distribution()
        gpa = self.gradebook.gpa()
        print(f"{total_courses} completed courses, a total of {total_credits} credits")
        print(f"mean {gpa}")
        print("grade distribution")
        for key, value in grade_distribution.items():
            print(f"{key}: " + "x" * value)


    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.get_entry()
            elif command == "3":
                self.get_statistics()
            else:
                self.help()

if __name__ == "__main__":
    application = CourseRecordApplication()
    application.execute()



