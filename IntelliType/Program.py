import sys
import subprocess
import shlex
import _thread
import os


def run_program_in_thread(command: str):
    is_windows = sys.platform.startswith('win')
    if is_windows:
        subprocess.Popen(shlex.split(command))
    else:
        os.system(command)


class Program:
    def __init__(self, command: str):
        self.command = command
        self.prepare_command()
        self.process = None

    def execute(self):
        print("HALLO WELT")
        thread = _thread.start_new_thread(run_program_in_thread,(self.command,))

    def prepare_command(self):
        return
