import keyboard
import random
import time


def str_to_seconds(value: str):
    try:
        if value.endswith('ms'):
            value = value.replace('ms','')
            denumerator = 1000
        elif value.endswith('s'):
            value = value.replace('s', '')
            denumerator = 1
        elif value.endswith('m'):
            value = value.replace('m', '')
            denumerator = 1 / 60
        elif value.endswith('h'):
            value = value.replace('h', '')
            denumerator = 1 / 3600
        else:
            print("Not valid time format " + value + "! Fallback to no time")
            return 0
        return int(value) / denumerator
    except ValueError:
        print("Not valid time format "+value + "! Fallback to no time")
        return 0


class Time:
    def __init__(self, t: str):
        self.t = str_to_seconds(t)

    def get_time_in_seconds(self):
        return self.t


class Keyspeed:
    def __init__(self, speed: str = 'FAST'):
        self.speed = speed

    def get_speed(self):
        value: str = self.speed
        if value.upper() == 'FAST':
            return 0.01
        if value.upper() == 'SLOW':
            return 1
        if value.upper() == 'MEDIUM':
            return 0.2
        if value.upper() == 'HUMAN':
            return 0.15 + random.uniform(-0.15, 0)
        return Time(value).get_time_in_seconds()


class Cmd:
    def __init__(self, command: str,keyspeed: Keyspeed):
        self.command = command + '\n'
        self.keyspeed = keyspeed

    def execute(self):
        keyboard.write(self.command,self.keyspeed.get_speed())


class Ctrl:
    def __init__(self,ctrl: str):
        self.ctrl = ctrl

    def execute(self):
        keyboard.press_and_release(self.ctrl)


class Text:
    def __init__(self, text: str, keyspeed: Keyspeed):
        self.text = text
        self.keyspeed = keyspeed

    def execute(self):
        for x in self.text:
            keyboard.write(x, self.keyspeed.get_speed())


class Wait:
    def __init__(self, t: Time):
        self.delay = t

    def execute(self):
        time.sleep(self.delay.get_time_in_seconds())
