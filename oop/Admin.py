from Users import Users
from Passengers import Passengers
from Tickets import Tickets

class Admin:
    users = Users()
    passengers = Passengers(200)
    tickets = Tickets(200)
    
    tickets_data_init = [
        {
            'ticket code' : '81N2O0',
            'train code' : 'Penataran Dhoho',
            'departure station' : 'Stasiun Malang',
            'departure time' : '08:23',
            'destination station' : 'Stasiun Wonokromo',
            'arrival time' : '10:34',
            'carriage' : 4,
            'sitting position' : '16A'
        },
        {
            'ticket code' : '98YB87',
            'train code' : 'Gajayana',
            'departure station' : 'Stasiun Gubeng',
            'departure time' : '16:21',
            'destination station' : 'Stasiun Blitar',
            'arrival time' : '22:35',
            'carriage' : 5,
            'sitting position' : '11D'
        },
        {
            'ticket code' : '1JH2B8',
            'train code' : 'Penataran Dhoho',
            'departure station' : 'Stasiun Solo Balapan',
            'departure time' : '04:40',
            'destination station' : 'Stasiun Kertosono',
            'arrival time' : '13:45',
            'carriage' : 5,
            'sitting position' : '12A'
        }, 
        {
            'ticket code' : 'KAS12K',
            'train code' : 'Penataran Dhoho',
            'departure station' : 'Stasiun Banyuwangi',
            'departure time' : '10:15',
            'destination station' : 'Stasiun Jember',
            'arrival time' : '12:30',
            'carriage' : 4,
            'sitting position' : '12C'
        },
        {
            'ticket code' : 'VAKJ12',
            'train code' : 'Gajayana',
            'departure station' : 'Stasiun Gubeng',
            'departure time' : '16:15',
            'destination station' : 'Stasiun Sidoarjo',
            'arrival time' : '18:30',
            'carriage' : 2,
            'sitting position' : '5B'
        }
    ]
    users_data_init = [
        {
            'name' : 'Hartanto',
            'email' : 'hartantowowo@example.com',
            'date of birth' :'10-12-1976'
        },
        {
            'name' : 'Angel',
            'email' : 'angelicadwi1@example.com',
            'date of birth' : '18-08-2001'
        },
        {
            'name' : 'Joe',
            'email' : 'johndoe@example.com',
            'date of birth' : '10-10-1990'
        },
        {
            'name' : 'Rose',
            'email' : 'roseviolet@example.com',
            'date of birth' : '15-05-1985'
        },
        {
            'name' : 'Mekar',
            'email' : 'mekarsari1298@example.com',
            'date of birth' : '12-09-1998'
        },
        {
            'name' : 'Handoyo',
            'email' : 'hanhandoyocuy@example.com',
            'date of birth' : '28-03-1962'
        },
        {
            'name' : 'Henry',
            'email' : 'henrysetiawan@example.com',
            'date of birth' : '27-02-2003'
        },
        {
            'name' : 'Billy',
            'email' : 'billyjoe@example.com',
            'date of birth' : '29-20-1994'
        }
    ]
    
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
            
    def add_users_data(self):
        for user in self.users_data_init:
            self.users.add_user(user['name'], user['email'], user['date of birth'])
    
    def add_tickets_data(self):
        for ticket in self.tickets_data_init:
            self.tickets.add_ticket_data(ticket['ticket code'], ticket['train code'], ticket['departure station'], ticket['departure time'], ticket['destination station'], ticket['arrival time'], ticket['carriage'], ticket['sitting position'])
    
    def add_passengers_data(self):
        for i in range(len(self.tickets_data_init)):
            self.passengers.add_passenger_data(self.users.users_data[i], self.tickets.tickets_data[i])
    