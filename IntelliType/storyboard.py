import yaml
import sys
import random
import time
import subprocess
import shlex
import _thread
import os
from IntelliType.storyvalues import Wait, Time, Keyspeed, Text, Ctrl, Cmd


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


class Scene:
    def __init__(self, program : Program, delay, countdown):
        self.program = program
        self.delay = delay
        self.countdown = countdown

    def run(self,nextSzenario = None):
        self.program.execute()
        if self.delay is None:
            self.program.execute()
            return
        if self.countdown is not None:
            if self.countdown:
                print(' Program starts in' )
                for i in range(0,int(self.delay)):
                    print(self.delay-i)
                    time.sleep(1)
            else:
                time.sleep(self.delay)
        else:
            time.sleep(self.delay)


class Section:
    def __init__(self, section_name : str):
        self.section_name = section_name
        self.items = []

    def add(self,item):
        self.items.append(item)

    def run(self):
        for x in self.items:
            x.execute()


class StoryScript:
    def __init__(self,filename : str):
        try:
            self.script_file = open(filename, 'r')
            self.file_content = yaml.safe_load(self.script_file)
            self.scene = None
            self.sections = []
        except OSError as err:
            print(err)
            sys.exit(-1)
        except SystemError as err:
            print(err)
            sys.exit(-1)

    def parse(self):
        for key, value in self.file_content.items():
            if key == 'scene':
                self.parse_scene(value)
            elif key == 'sections':
                self.parse_sections(value)
            else:
                print("Unsupported key " + key + " in root level was found! Will be ignored")

    def parse_scene(self,scene: dict):
        command = None
        delay = None
        countdown = None
        for key, value in scene.items():
            if key == 'program':
                command = value
            elif key == 'wait':
                delay = Time(value).get_time_in_seconds()
            elif key == 'countdown':
                countdown = value
            else:
                print("Unsupported key " + key + " in scene level was found! Will be ignored")

        self.scene = Scene(Program(command), delay, countdown)


    def parse_sections(self, sections:dict):
        for section_name, l in sections.items():
            section = Section(section_name)
            for process_items in l:
                values = process_items.items()
                speed_stack = [Keyspeed()]
                for key,value in values:
                    if key.upper() == "WAIT":
                        section.add(Wait(Time(value)))
                    elif key.upper() == "KEYSPEED" :
                        speed_stack.append(Keyspeed(value))
                    elif key.upper() == "TEXT":
                        section.add(Text(value,speed_stack.pop()))
                        if len(speed_stack) == 0:
                            speed_stack.append(Keyspeed())
                    elif key.upper() == "CTRL":
                        section.add(Ctrl(value))
                    elif key.upper() == "CMD":
                        section.add(Cmd(value,speed_stack.pop()))
                        if len(speed_stack) == 0:
                            speed_stack.append(Keyspeed())
                    else:
                        print("Unexpected key " + key + " in section " + section_name)
            self.sections.append(section)