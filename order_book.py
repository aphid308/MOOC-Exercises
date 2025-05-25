

class Task:
    newid = 0
    def __init__(self, description: str, programmer: str, workload: int, finished=False):
        Task.newid += 1
        self.id = Task.newid
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = finished

    def is_finished(self):
        if self.finished:
            return True
        else:
            return False

    def mark_finished(self):
        self.finished = True

    def __str__(self):
        return (f"{self.id}: {self.description} ({self.workload} hours), "
                f"{self.programmer} {'FINISHED' if self.is_finished() else 'NOT FINISHED'}")

class OrderBook:
    def __init__(self):
        self.__orders = {}

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        self.__orders[task.id] = task

    def all_orders(self):
        return self.__orders.values()

    def programmers(self):
        programmers = [order.programmer for order in self.__orders.values()]
        return list(set(programmers))

    def mark_finished(self, id: int):
        if id in self.__orders.keys():
            order = self.__orders[id]
            order.mark_finished()
        else:
            raise ValueError("id not in orderbook")

    def finished_orders(self):
        return [order for order in self.all_orders() if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.all_orders() if not order.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer in self.programmers():
            finished_tasks = [order for order in self.finished_orders() if order.programmer == programmer]
            unfinished_tasks = [order for order in self.unfinished_orders() if order.programmer == programmer]
            total_finished_hours = sum([order.workload for order in finished_tasks])
            total_unfinished_hours = sum([order.workload for order in unfinished_tasks])
            return len(finished_tasks), len(unfinished_tasks), total_finished_hours, total_unfinished_hours
        else:
            raise ValueError("programmer not in orderbook")

class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark tasks as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                try:
                    self.add_order()
                except ValueError:
                    print("erroneous input")
                    continue
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                try:
                    self.mark_task_finished()
                except ValueError:
                    print("erroneous input")
                    continue
            elif command == "5":
                self.programmers()
            elif command == "6":
                try:
                    self.status_of_programmer()
                except ValueError:
                    print("erroneous input")
                    continue
            else:
                self.help()
    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()
        workload = int(workload)
        self.__orderbook.add_order(description, programmer, workload)
        print("added!")

    def list_finished_tasks(self):
        if self.__orderbook.finished_orders():
            for order in self.__orderbook.finished_orders():
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        if self.__orderbook.unfinished_orders():
            for order in self.__orderbook.unfinished_orders():
                print(order)
        else:
            print("no unfinished tasks")

    def mark_task_finished(self):
        id = int(input("id: "))
        self.__orderbook.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        programmer_status = self.__orderbook.status_of_programmer(programmer)
        print(f"tasks: finished {programmer_status[0]} not finished {programmer_status[1]}, hours: done {programmer_status[2]} scheduled {programmer_status[3]}")

if __name__ == "__main__":
    application = OrderBookApplication()
    application.execute()
