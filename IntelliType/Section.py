import keyboard
import time
import random
class Section:
    def __init__(self,keyspeed=None,text = None,cmd = None,ctrl = None,delay = None):
        self.keyspeed = keyspeed
        self.text = text
        self.cmd = cmd
        self.ctrl = ctrl
        self.delay = delay

    def run(self):
        speed = 0
        human = False;
        if self.keyspeed is not None:
            if self.keyspeed == 'HUMAN':
                human = True
            else:
                speed = self.get_keyspeed()
        if self.text is not None:
            if human:
                self.write_human()
            else:
                keyboard.write(self.text, speed)
        elif self.cmd is not None:
            if human:
                self.write_human(self.cmd+'\n')
            else:
                keyboard.write(self.cmd+'\n', speed)
        elif self.ctrl is not None:
            keyboard.press_and_release(self.ctrl)
        if self.delay is not None:
           time.sleep(self.delay)

    def get_keyspeed(self):
        value :str = self.keyspeed
        if value.upper() == 'FAST':
            return 0.01
        if value.upper() == 'SLOW':
            return 1
        if value.upper() == 'MEDIUM':
            return 0.2
        return 0

    def write_human(self):
        for x in self.text:
            val = random.uniform(-0.15, 0);
            keyboard.write(x, 0.15 + val)