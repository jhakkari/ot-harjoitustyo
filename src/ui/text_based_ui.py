from repositories import user_repository

class TextBasedUi:

    def start(self):
        OpeningScreen().start()


class OpeningScreen:

    def __init__(self):
        self.commands = {
            "X": "X quit application"}

    def start(self):
        while True:
            print("Nothing to see, yet!")
            print(self.commands)

            command = input("> ")

            if not command in self.commands:
                print("command not found")

            if command == "X":
                break



