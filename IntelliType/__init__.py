import sys
from IntelliType.storyboard import StoryScript


def run():
    if len(sys.argv) < 2:
        print("Usage: itt script.yaml")
    else:
        story_script = StoryScript(sys.argv[1])
        story_script.parse()
        story_script.scene.run()
        for x in story_script.sections:
            x.run()


if __name__ == '__main__':
    run()
