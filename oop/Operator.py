import time
import locale

from DepartureGate import DepartureGate
from Platform import Platform
from Queue import Queue

class Operator:
    gate = DepartureGate()
    platform = Platform(250)
    
    def __init__(self, name, age, passengers, tickets, users, waiting_space) -> None:
        self.name = name
        self.age = age
        self.passengers = passengers
        self.tickets = tickets
        self.waiting_space = waiting_space
        self.queue = Queue(10, tickets, users)
        self.train_schedules = [
            'Penataran Dhoho',
            'Gajayana',
            'Argo Lawu'
        ]
        self.current_train = 0
        self.current_user = None

    def check_user_data(self):
        queuer = self.queue.check_queuer_data()
        if queuer and queuer.ticket and queuer.user:
            print('Kode tiket : ', queuer.ticket.ticket_code)
            print('Nama : ', queuer.user.name)
            print('Kode kerata : ', queuer.ticket.train_code)
            print('Stasiun awal : ', queuer.ticket.departure_station, '/', queuer.ticket.departure_time)
            print('Stasiun tujuan : ', queuer.ticket.destination_station, '/', queuer.ticket.arrival_time)
            print('Gerbong : ', queuer.ticket.carriage)
            print('Posisi duduk: ', queuer.ticket.sitting_position)
            print('\n')
            
            self.check_actual_queuer_data(queuer)
        else:
            print('Penumpang tidak valid!')
            print('\n')
        
        self.update_queue_data(queuer)
        input('Lanjutkan => ')
    
    def check_actual_queuer_data(self, queuer):
        user_input_confirmation = str(input('Cek data aktual ? [y/n] '))
        if user_input_confirmation == 'y':
            actual_user = self.passengers.check_user_data(queuer.ticket.ticket_code)
            
            if actual_user:
                print('============================================')
                print('Kode tiket : ', actual_user.ticket.ticket_code)
                
                is_found_data_not_match = False
                if queuer.user.name != actual_user.user.name:
                    is_found_data_not_match = True
                    print('\033[31mNama : ', actual_user.user.name, '\033[0m')
                else:
                    print('Nama : ', actual_user.user.name)
                
                if queuer.ticket.train_code != actual_user.ticket.train_code:
                    print('\033[31mKode kerata : ', queuer.ticket.train_code, '\033[0m')
                else:
                    print('Kode kerata : ', queuer.ticket.train_code)
                
                if queuer.ticket.departure_station != actual_user.ticket.departure_station:
                    is_found_data_not_match = True
                    print('\033[31mStasiun awal : ', actual_user.ticket.departure_station, '/', actual_user.ticket.departure_time, '\033[0m')
                else:
                    print('Stasiun awal : ', actual_user.ticket.departure_station, '/', actual_user.ticket.departure_time)
                    
                if queuer.ticket.destination_station != actual_user.ticket.destination_station:
                    is_found_data_not_match = True
                    print('\033[31mStasiun tujuan : ', actual_user.ticket.destination_station, '/', actual_user.ticket.arrival_time, '\033[0m')
                else:
                    print('Stasiun tujuan : ', actual_user.ticket.destination_station, '/', actual_user.ticket.arrival_time)
                    
                if queuer.ticket.carriage != actual_user.ticket.carriage:
                    is_found_data_not_match = True
                    print('\033[31mGerbong : ', actual_user.ticket.carriage, '\033[0m')
                else:
                    print('Gerbong : ', actual_user.ticket.carriage)
                
                if queuer.ticket.sitting_position != actual_user.ticket.sitting_position:
                    is_found_data_not_match = True
                    print('\033[31mPosisi duduk: ', actual_user.ticket.sitting_position, '\033[0m')
                else:
                    print('Posisi duduk: ', actual_user.ticket.sitting_position)
                    
                print('\n')
                
                if not is_found_data_not_match:
                    queuer.is_valid = True
                    self.current_user = queuer
                else:
                    print('Data penumpang tidak valid!')
            else:
                print('Data pengguna tidak ditemukan!')
                print('\n')
    
    def update_queue_data(self, queuer):
        if queuer.is_valid:
            self.waiting_space.add_people_to_waiting_space(self.queue.queuers[0])
        
        self.queue.rearrange_queue()
        self.queue.add_queue()
    
    def check_user_stuffs(self):
        if self.current_user != None:
            stuffs = self.current_user.stuffs
            if stuffs:
                for stuff in stuffs.stuffs_data:
                    print('Nama barang: ', stuff.name)
                    print('Berat: ', stuff.weight, 'kg')
                    print('Ukuran: p=', stuff.length, 'cm, l=', stuff.width, 'cm, t=', stuff.height, 'cm')
                    print('-----------------------------------------')
                input('Lanjutkan => ')
                self.calculate_user_fine(stuffs)
                self.current_user = None
            else: 
                print('Penumpang tidak membawa barang bawaan apapun')
        else:
            print('Pastikan penumpang memiliki tiket yang valid terlebih dahulu!')
        
        input('\nLanjutkan => ')

    def calculate_user_fine(self, stuffs):
        print('Menghitung denda yang didapat')
        total_fine = 0
        for stuff in stuffs.stuffs_data:
            volume = stuff.length * stuff.width * stuff.height
            weight = stuff.weight
            
            if volume > 30000:
                total_fine += volume % 30000 / 5000 * 10000
            
            if weight > 5:
                total_fine += weight % 5 * 5000
        
        self.current_user.fine = total_fine
        locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')
        print('Penumpang akan dikenakan denda sebesar Rp ', locale.currency(total_fine, grouping=True))

    def open_departure_gate(self, train_code):
        if self.current_train < len(self.train_schedules):
            self.gate.open_gate()
            for people in self.waiting_space.peoples:
                print('mencoba!')
                if people.ticket.train_code == train_code:
                    self.platform.add_people_to_platform(self.waiting_space.move_people(people))
                    print(people.user.name, ' memasuki peron')
                    time.sleep(0.5)
            
            self.current_train += 1
        else:
            print('Tidak ada jadwal kereta yang tersedia lagi!')
        
        input('Lanjutkan => ')
        
    def close_departure_gate(self):
        self.gate.close_gate()
        input('Lanjutkan => ')