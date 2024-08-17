class WaitingSpace:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.peoples = []
        
    def add_people_to_waiting_space(self, people):
        if len(self.peoples) < self.capacity:
            self.peoples.append(people)
        else:
            print('Ruang tunggu masih penuh! Penumpang dimohon untuk menunggu di area lain')
    
    def move_people(self, people):
        data = list(filter(lambda data : data == people, self.peoples))[0]
        self.peoples.remove(data)
        return data
