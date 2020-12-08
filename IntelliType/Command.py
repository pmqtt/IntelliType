from IntelliType.Keyspeed import Keyspeed
import keyboard

class Cmd:
    def __init__(self,command: str,keyspeed: Keyspeed):
        self.command = command + '\n'
        self.keyspeed = keyspeed

    def execute(self):
        keyboard.write(self.command,self.keyspeed.get_speed())