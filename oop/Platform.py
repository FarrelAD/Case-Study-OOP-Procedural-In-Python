class Platform:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.peoples = []
        self.total_people = 0
        
    def add_people_to_platform(self, people):
        if self.total_people < self.capacity:
            self.peoples.append(people)