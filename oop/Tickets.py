from Ticket import Ticket

class Tickets:
    def __init__(self, length) -> None:
        self.length = length
        self.size = 0
        self.tickets_data = []
    
    def add_ticket_data(self, ticket_code, train_code, departure_station, departure_time, destination_station, arrival_time, carriage, sitting_position):
        if self.size < self.length:
            self.tickets_data.append(Ticket(ticket_code, train_code, departure_station, departure_time, destination_station, arrival_time, carriage, sitting_position))
            self.size += 1
        else:
            print('Data tiket sudah memenuhi kapasitas!')