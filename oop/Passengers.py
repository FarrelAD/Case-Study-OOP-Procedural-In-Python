from Passenger import Passenger

class Passengers:
    def __init__(self, length) -> None:
        self.length = length
        self.size = 0
        self.passengers_data = []
        
    def add_passenger_data(self, user, ticket):
        if self.size < self.length:
            self.passengers_data.append(Passenger(user, ticket))
            self.size += 1
        else:
            print('Penumpang sudah memenuhi kapasitas kereta!')
    
    def check_user_data(self, user_ticket) -> Passenger:
        for data in self.passengers_data:
            if data.ticket.ticket_code == user_ticket:
                return data
        return None