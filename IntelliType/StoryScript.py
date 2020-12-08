import yaml
from IntelliType import Program, Scene, Section, Wait, Keyspeed, Text, Control, Command
from IntelliType.Time import Time
import sys


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

    def parse_scene(self,scene : dict):
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

        self.scene = Scene.Scene(Program.Program(command), delay, countdown)


    def parse_sections(self, sections:dict):
        for section_name, l in sections.items():
            section = Section.Section(section_name)
            for process_items in l:
                values = process_items.items()
                speed_stack = [Keyspeed.Keyspeed()]
                for key,value in values:
                    if key.upper() == "WAIT":
                        section.add(Wait.Wait(Time(value)))
                    elif key.upper() == "KEYSPEED" :
                        speed_stack.append(Keyspeed.Keyspeed(value))
                    elif key.upper() == "TEXT":
                        section.add(Text.Text(value,speed_stack.pop()))
                        if len(speed_stack) == 0:
                            speed_stack.append(Keyspeed.Keyspeed())
                    elif key.upper() == "CTRL":
                        section.add(Control.Ctrl(value))
                    elif key.upper() == "CMD":
                        section.add(Command.Cmd(value,speed_stack.pop()))
                        if len(speed_stack) == 0:
                            speed_stack.append(Keyspeed.Keyspeed())
                    else:
                        print("Unexpected key " + key + " in section " + section_name)
            self.sections.append(section)