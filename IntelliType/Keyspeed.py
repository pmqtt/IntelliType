import random
from IntelliType import Time

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
        return Time.Time(value).get_time_in_seconds()
