import os


class Program:

    def __init__(self, command: str):
        self.command = command
        self.prepare_command()

    def execute(self):
        os.system(self.command)

    def prepare_command(self):
        return
