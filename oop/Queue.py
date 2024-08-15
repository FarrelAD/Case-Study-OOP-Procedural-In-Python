class Queue:
    is_valid = False
    fine = 0
    
    def __init__(self, queue_id, passenger, ticket) -> None:
        self.queue_id = queue_id
        self.passenger = passenger
        self.ticket = ticket