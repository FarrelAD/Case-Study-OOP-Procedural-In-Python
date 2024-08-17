from Stuff import Stuff

class Stuffs:
    def __init__(self) -> None:
        self.stuffs_data = []
        
    def add_stuffs(self, name, weight, length, width, height):
        self.stuffs_data.append(Stuff(name, weight, length, width, height))