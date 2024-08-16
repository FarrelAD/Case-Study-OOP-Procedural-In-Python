class WaitingSpace:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.total_people = 0
        self.peoples = []
        
    def add_people_to_waiting_space(self, people):
        if self.total_people < self.capacity:
            self.peoples.append(people)
            self.total_people += 1
        else:
            print('Ruang tunggu masih penuh! Penumpang dimohon untuk menunggu di area lain')
    
    def move_people(self, people):
        return list(filter(lambda data : data == people, self.peoples))