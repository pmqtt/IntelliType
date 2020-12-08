import time
from IntelliType import Time

class Wait:
    def __init__(self, t: Time):
        self.delay = t

    def execute(self):
        time.sleep(self.delay.get_time_in_seconds())
