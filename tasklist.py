class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name: str, priority: int):
        self.tasks.append((priority, name))

    def get_next(self):
        self.tasks.sort()
        # The list method pop removes and returns the last item in a list
        task = self.tasks.pop()
        # Return the name of the task (the second item in the tuple)
        return task[1]

    def number_of_tasks(self):
        return len(self.tasks)

    def clear_tasks(self):
        self.tasks = []

if __name__ == '__main__':
    tasks = TaskList()
    tasks.add_task("studying", 50)
    tasks.add_task("exercise", 60)
    tasks.add_task("cleaning", 10)
    print(tasks.number_of_tasks())
    print(tasks.get_next())
    print(tasks.number_of_tasks())
    tasks.add_task("date", 100)
    print(tasks.number_of_tasks())
    print(tasks.get_next())
    print(tasks.get_next())
    print(tasks.number_of_tasks())
    tasks.clear_tasks()
    print(tasks.number_of_tasks())