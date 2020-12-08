import random



class Section:
    def __init__(self, section_name : str):
        self.section_name = section_name
        self.items = []

    def add(self,item):
        self.items.append(item)

    def run(self):
        for x in self.items:
            x.execute()



