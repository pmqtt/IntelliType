import keyboard

class Ctrl:
    def __init__(self,ctrl: str):
        self.ctrl = ctrl

    def execute(self):
        keyboard.press_and_release(self.ctrl)