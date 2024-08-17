from Queuer import Queuer
from Stuffs import Stuffs

class Queue:
    def __init__(self, length, tickets, users) -> None:
        self.length = length
        
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

        self.users_bring_stuffs = [
            {
                'name' : 'Hartanto',
                'stuffs' :
                    [
                        {
                            'name' : 'tas ransel',
                            'weight' : 3,
                            'length' : 30,
                            'width' : 20,
                            'height' : 70
                        },
                        {
                            'name' : 'koper',
                            'weight' : 7,
                            'length' : 40,
                            'width' : 35,
                            'height' : 70
                        }
                    ]
            },
            {
                'name' : 'Angel',
                'stuffs' : 
                    [
                        {
                            'name' : 'helm Arai',
                            'weight' : 2,
                            'length' : 35,
                            'width' : 35,
                            'height' : 35
                        }
                    ]
            },
            {
                'name' : 'Rose',
                'stuffs' : 
                    [
                        {
                            'name' : 'Knalpot R15',
                            'weight' : 3,
                            'length' : 2,
                            'width' : 0.2,
                            'height' : 0.5
                        }
                    ]
            }
        ]
    
    
        self.current_max_index = 9
        self.queuers = []
        
        for i in range(10):
            self.queuers.append(Queuer(ticket=self.all_queue_data[i]['ticket'], user=self.all_queue_data[i]['user']))
            if self.queuers[i].user != None and any(data['name'] == self.queuers[i].user.name for data in self.users_bring_stuffs):
                user_index = -1
                for j, d in enumerate(self.users_bring_stuffs):
                    if d['name'] == self.queuers[i].user.name:
                        user_index = j
                        break
                
                user_stuffs_input = self.users_bring_stuffs[user_index]['stuffs']
                user_stuffs = Stuffs()
                for stuff in user_stuffs_input:
                    user_stuffs.add_stuffs(name=stuff['name'], weight=stuff['weight'], length=stuff['length'], width=stuff['width'], height=stuff['height'])
                    
                self.queuers[i].stuffs = user_stuffs

    def check_queuer_data(self) -> Queuer:
        if len(self.queuers) >= 0:
            return self.queuers[0]
        else:
            print('Antrian kosong!')
            return None
    
    def add_queue(self):
        if len(self.queuers) < self.length and self.current_max_index < len(self.all_queue_data) - 1:
            data = self.all_queue_data[self.current_max_index + 1]
            self.queuers.append(Queuer(ticket=data['ticket'], user=data['user']))
        else:
            print('Antrian masih penuh!')

    def rearrange_queue(self):
        for i in range(len(self.queuers) - 1):
            self.queuers[i] = self.queuers[i + 1]
        
        self.queuers.pop()