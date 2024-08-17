import os
import platform

from Admin import Admin
from Operator import Operator
from WaitingSpace import WaitingSpace

def display_main_menu():
    return int(
input('''
1. Cek data pengguna
2. Cek barang bawaan pengguna
3. Buka pintu masuk
4. Keluar
'''))

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def main():
    admin = Admin('Hana', 27)
    admin.add_users_data()
    admin.add_tickets_data()
    admin.add_passengers_data()
    
    waiting_space = WaitingSpace(400)
    
    operator = Operator(name='Budi', age=37, passengers=admin.passengers, tickets=admin.tickets, users=admin.users, waiting_space=waiting_space)
    
    
    user_input_menu = 1
    while user_input_menu < 5 and user_input_menu > 0:
        clear_terminal()
        print('Antrian saat ini [', len(operator.queue.queuers), '/ 10 ]')
        user_input_menu =  display_main_menu()
        if user_input_menu == 1:
            operator.check_user_data()
        elif user_input_menu == 2:
            operator.check_user_stuffs()
        elif user_input_menu == 3:
            operator.open_departure_gate(operator.train_schedules[operator.current_train])
        elif user_input_menu == 4:
            exit()

if __name__ == '__main__':
    main()