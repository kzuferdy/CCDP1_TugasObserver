from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ShowFloraInfoCommand(Command):
    def __init__(self, flora_name):
        self.flora_name = flora_name

    def execute(self):
        # Lakukan tindakan untuk menampilkan informasi tentang flora
        print("Menampilkan informasi flora tentang:", self.flora_name)


class ShowFaunaInfoCommand(Command):
    def __init__(self, fauna_name):
        self.fauna_name = fauna_name

    def execute(self):
        # Lakukan tindakan untuk menampilkan informasi tentang fauna
        print("Menampilkan informasi fauna tentang:", self.fauna_name)

class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        if self.command is not None:
            self.command.execute()

def main():
    # Membuat objek-invoker
    invoker = Invoker()

    # Membuat objek-command untuk menampilkan informasi flora dan fauna
    show_flora_info_command = ShowFloraInfoCommand("Mawar")
    show_fauna_info_command = ShowFaunaInfoCommand("Harimau")

    # Menampilkan informasi flora
    invoker.set_command(show_flora_info_command)
    invoker.execute_command()

    # Menampilkan informasi fauna
    invoker.set_command(show_fauna_info_command)
    invoker.execute_command()


if __name__ == "__main__":
    main()
