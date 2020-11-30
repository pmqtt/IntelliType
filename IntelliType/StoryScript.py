import yaml
from IntelliType import Program, Scene, Section


def str_to_seconds(value: str):
    try:
        if value.endswith('ms'):
            value = value.replace('ms','')
            denum = 1000
        elif value.endswith('s'):
            value = value.replace('s', '')
            denum = 1
        elif value.endswith('m'):
            value = value.replace('m', '')
            denum = 1/60
        elif value.endswith('h'):
            value = value.replace('h', '')
            denum = 1/3600
        else:
            print("Not valid time format " + value + "! Fallback to notime")
            return 0
        return int(value)/denum
    except ValueError:
        print("Not valid time format "+value +"! Fallback to notime")
        return 0


class StoryScript:
    def __init__(self,filename : str):
        self.script_file = open(filename,'r')
        self.file_content = yaml.safe_load(self.script_file)
        self.scene = None
        self.sections = []
    def parse(self):
        for key,value in self.file_content.items():
            if key == 'scene':
                self.parse_scene(value)
            elif key.startswith('section'):
                self.parse_section(value)
            else:
                print("Unsuported key " + key + " in root level was found! Will be ignored")

    def parse_scene(self,scene : dict):
        command = None
        delay = None
        countdown = None
        for key,value in scene.items():
            if key == 'program':
                command = value
            elif key == 'wait':
                delay = str_to_seconds(value)
            elif key == 'countdown':
                countdown = value
            else:
                print("Unsuported key " + key + " in scene level was found! Will be ignored")

        self.scene = Scene.Scene(Program.Program(command), delay, countdown)


    def parse_section(self, section:dict):
        text = None
        keyspeed = None
        ctrl = None
        cmd = None
        delay = None
        for key,value in section.items():
            if key == 'text':
                text = value
            elif key == 'keyspeed':
                keyspeed =value
            elif key == 'ctrl':
                ctrl = value;
            elif key == 'cmd':
                cmd = value;
            elif key == 'wait':
                delay = str_to_seconds(value)
            else:
                "Unsuported key " + key + " in section level was found! Will be ignored"

        self.sections.append(Section.Section(keyspeed, text, cmd, ctrl, delay))
