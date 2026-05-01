# ===============================
# 1. Singleton Pattern
# ===============================
class TaskManager:
    __instance = None

    def __init__(self):
        if TaskManager.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.tasks = []
            TaskManager.__instance = self

    @staticmethod
    def get_instance():
        if TaskManager.__instance is None:
            TaskManager()
        return TaskManager.__instance

    def add_task(self, task):
        self.tasks.append(task)

    def show_tasks(self):
        for task in self.tasks:
            print(task)


# ===============================
# 2. Factory Pattern
# ===============================
class Task:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Task: {self.name}"


class WorkTask(Task):
    def __str__(self):
        return f"Work Task: {self.name}"


class PersonalTask(Task):
    def __str__(self):
        return f"Personal Task: {self.name}"


class TaskFactory:
    @staticmethod
    def create_task(task_type, name):
        if task_type == "work":
            return WorkTask(name)
        elif task_type == "personal":
            return PersonalTask(name)
        else:
            raise ValueError("Invalid task type")


# ===============================
# 3. Observer Pattern
# ===============================
class Observer:
    def update(self, message):
        pass


class User(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received update: {message}")


class NotificationSystem:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


# ===============================
# Main Program
# ===============================
if __name__ == "__main__":
    # Singleton
    manager = TaskManager.get_instance()

    # Factory
    task1 = TaskFactory.create_task("work", "Finish report")
    task2 = TaskFactory.create_task("personal", "Go to gym")

    manager.add_task(task1)
    manager.add_task(task2)

    manager.show_tasks()

    # Observer
    notification_system = NotificationSystem()

    user1 = User("Omar")
    user2 = User("Ali")

    notification_system.subscribe(user1)
    notification_system.subscribe(user2)

    notification_system.notify("New task added!")
