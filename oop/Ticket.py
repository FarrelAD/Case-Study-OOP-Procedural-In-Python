class Ticket:
    def __init__(self, ticket_code, train_code, departure_station, departure_time, destination_station, arrival_time, carriage, sitting_position) -> None:
        self.ticket_code = ticket_code
        self.train_code = train_code
        self.departure_station = departure_station
        self.departure_time = departure_time
        self.destination_station = destination_station
        self.arrival_time = arrival_time
        self.carriage = carriage
        self.sitting_position = sitting_position