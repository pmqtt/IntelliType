from IntelliType import Program
import time


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
                    time.sleep(1);
            else:
                time.sleep(self.delay)
        else:
            time.sleep(self.delay)


