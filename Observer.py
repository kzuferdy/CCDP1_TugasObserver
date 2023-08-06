class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class User:
    def __init__(self, name):
        self._name = name

    def update(self, message):
        print(f"{self._name} received notification: {message}")


# Contoh penggunaan Observer Pattern
subject = Subject()
user1 = User("Alice")
user2 = User("Bob")

subject.attach(user1)
subject.attach(user2)

subject.notify("New content on Flora and Fauna")
