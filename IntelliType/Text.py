import keyboard

from IntelliType.Keyspeed import Keyspeed


class Text:
    def __init__(self, text: str, keyspeed: Keyspeed):
        self.text = text
        self.keyspeed = keyspeed

    def execute(self):
        for x in self.text:
            keyboard.write(x,self.keyspeed.get_speed())
