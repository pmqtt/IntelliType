# This is a sample Python script.
from IntelliType import StoryScript
import sys;


def run():
    if len(sys.argv) < 2:
        print("Usage: itt script.yaml")
    else:
        story_script = StoryScript.StoryScript(sys.argv[1])
        story_script.parse()
        story_script.scene.run()
        for x in story_script.sections:
            x.run()



if __name__ == '__main__':
    run()
