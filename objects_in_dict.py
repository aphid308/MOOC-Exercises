class ExerciseCounter:
    def __init__(self):
        self.__exercises = 0

    def done(self):
        self.__exercises += 1

    def how_many(self):
        return self.__exercises

if __name__ == '__main__':
    students = {}

    print("let's do some exercises")
    while True:
        name = input("student: ")
        if len(name) == 0:
            break

        # create a new object if it doesn't exist yet
        if not name in students:
            students[name] = ExerciseCounter()

        # add a new done exercise to the counter
        students[name].done()

    print()
    print("exercises completed:")

    for student, exercises in students.items():
        print(f"{student}'s exercises: {exercises.how_many()}")