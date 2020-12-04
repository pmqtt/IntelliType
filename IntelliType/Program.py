import sys
import subprocess
import shlex
import threading
import os

def run_program_in_thread(command: str):
    is_windows = sys.platform.startswith('win')
    if is_windows:
        DETACHED_PROCESS = 0x00000008
        subprocess.Popen(shlex.split(command), creationflags=DETACHED_PROCESS, shell=True, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)
    else:
        subprocess.Popen(shlex.split(command))


class Program:
    def __init__(self, command: str):
        self.command = command
        self.prepare_command()
        self.process = None

    def execute(self):
        pid = os.fork()
        if pid == 0:
            run_program_in_thread(self.command)
            sys.exit(0)

    def prepare_command(self):
        return
