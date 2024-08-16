from Queuer import Queuer

class Queue:
    
    def __init__(self, length, tickets, users) -> None:
        self.length = length
        self.size = 0
        
        # initialize all possible user that want to be in queue
        self.all_queue_data = [
            {
                'ticket' : None,
                'user' : None
            },
            {
                'ticket' : tickets.tickets_data[0],
                'user' : users.users_data[0]
            },
            {
                'ticket' : tickets.tickets_data[2],
                'user' : None
            },
            {
                'ticket' : tickets.tickets_data[2],
                'user' : users.users_data[3]
            },
            {
                'ticket' : tickets.tickets_data[1],
                'user' : users.users_data[3]
            },
            {
                'ticket' : tickets.tickets_data[4],
                'user' : users.users_data[4],
            },
            {
                'ticket' : None, 
                'user' : None
            },
            {
                'ticket' : None,
                'user' : users.users_data[1]
            },
            {
                'ticket' : None,
                'user' : None
            },
            {
                'ticket' : tickets.tickets_data[1],
                'user' : users.users_data[1]
            },
            {
                'ticket' : None,
                'user' : None
            },
            {
                'ticket' : tickets.tickets_data[2],
                'user' : users.users_data[2]
            }
        ]
        
        self.current_max_index = 9
        self.queuers = []
        
        for i in range(10):
            self.queuers.append(Queuer(ticket=self.all_queue_data[i]['ticket'], user=self.all_queue_data[i]['user']))
            self.size += 1
    
    def check_queuer_data(self) -> Queuer:
        if self.size >= 0:
            return self.queuers[0]
        else:
            print('Antrian kosong!')
            return None
    
    def add_queue(self):
        if self.size < self.length:
            data = self.all_queue_data[self.current_max_index + 1]
            self.queuers.append(Queuer(ticket=data['ticket'], user=data['user']))
            self.size += 1
        else:
            print('Antrian masih penuh!')
    
    def rearrange_queue(self):
        for i in range(self.length - 1):
            self.queuers[i] = self.queuers[i + 1]
        
        self.queuers.pop()
        self.size -= 1