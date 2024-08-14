# Sistem masuk kereta api
# Train entry system

import os
import platform
import locale
import time

locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

current_user = 0

def initialize_data():
    global users
    users = {
        1 : {
            'isValid' : False,
            'kode tiket' : '81N2O0',
            'nama' : 'Hartanto',
            'stasiun awal' : 'Stasiun Malang',
            'waktu keberangkatan' : '08:23',
            'stasiun tujuan' : 'Stasiun Wonokromo',
            'waktu kedatangan' : '10:34',
            'gerbong' : '4',
            'posisi duduk' : '16A',
            'barang' : {
                1 : {
                    'nama' : 'tas ransel',
                    'berat' : 3,
                    'ukuran' : {
                        'panjang' : 30,
                        'lebar' : 20,
                        'tinggi' : 70
                    }
                },
                2 : {
                    'nama' : 'koper',
                    'berat' : 7,
                    'ukuran' : {
                        'panjang' : 40,
                        'lebar' : 35,
                        'tinggi' : 70
                    }
                }
            },
            'denda' : 0
        },
        2 : {
            'isValid' : False,
            'kode tiket' : '98YB87',
            'nama' : 'Angel',
            'stasiun awal' : 'Stasiun Gubeng',
            'waktu keberangkatan' : '16:21',
            'stasiun tujuan' : 'Stasiun Blitar',
            'waktu kedatangan' : '22:35',
            'gerbong' : '1',
            'posisi duduk' : '11D',
            'barang' : {},
            'denda' : 0
        },
        3: {
            'isValid' : False,
            'kode tiket' : '1JH2B8',
            'nama' : 'Joe',
            'stasiun awal' : 'Stasiun Malang',
            'waktu keberangkatan' : '07:20',
            'stasiun tujuan' : 'Stasiun Mojokerto',
            'waktu kedatangan' : '13:45',
            'gerbong' : '',
            'posisi duduk' : '',
            'barang' : {
                1 : {
                    'nama' : 'helm Arai',
                    'berat' : 2,
                    'ukuran' : {
                        'panjang' : 35,
                        'lebar' : 35,
                        'tinggi' : 35
                    }
                }
            },
            'denda' : 0
        },
        4 : {
            'isValid' : False,
            'kode tiket' : 'KAS12K',
            'nama' : 'Rose',
            'stasiun awal' : 'Stasiun Banyuwangi',
            'waktu keberangkatan' : '10:15',
            'stasiun tujuan' : 'Stasiun Jember',
            'waktu kedatangan' : '12:30',
            'gerbong' : '4',
            'posisi duduk' : '12C',
            'barang' : {},
            'denda' : 0
        },
        5 : {
            'isValid' : False,
            'kode tiket' : 'VAKJ12',
            'nama' : 'Henry',
            'stasiun awal' : 'Stasiun Gubeng',
            'waktu keberangkatan' : '16:15',
            'stasiun tujuan' : 'Stasiun Sidoarjo',
            'waktu kedatangan' : '18:30',
            'gerbong' : '2',
            'posisi duduk' : '5B',
            'barang' : {},
            'denda' : 0
        }
    }
    
    global real_user
    real_user = {
        1 : {
            'kode tiket' : '81N2O0',
            'nama' : 'Hartanto',
            'stasiun awal' : 'Stasiun Malang',
            'waktu keberangkatan' : '08:23',
            'stasiun tujuan' : 'Stasiun Wonokromo',
            'waktu kedatangan' : '10:34',
            'gerbong' : '4',
            'posisi duduk' : '16A'
        },
        2 : {
            'kode tiket' : '98YB87',
            'nama' : 'Angel',
            'stasiun awal' : 'Stasiun Gubeng',
            'waktu keberangkatan' : '16:21',
            'stasiun tujuan' : 'Stasiun Blitar',
            'waktu kedatangan' : '22:35',
            'gerbong' : '5',
            'posisi duduk' : '11D'
        },
        3: {
            'kode tiket' : '1JH2B8',
            'nama' : 'Joe',
            'stasiun awal' : 'Stasiun Solo Balapan',
            'waktu keberangkatan' : '04:40',
            'stasiun tujuan' : 'Stasiun Kertosono',
            'waktu kedatangan' : '13:45',
            'gerbong' : '5',
            'posisi duduk' : '12A',
        },
        4 : {
            'isValid' : False,
            'kode tiket' : 'KAS12K',
            'nama' : 'Rose',
            'stasiun awal' : 'Stasiun Banyuwangi',
            'waktu keberangkatan' : '10:15',
            'stasiun tujuan' : 'Stasiun Jember',
            'waktu kedatangan' : '12:30',
            'gerbong' : '4',
            'posisi duduk' : '12C'
        },
        5 : {
            'isValid' : False,
            'kode tiket' : 'VAKJ12',
            'nama' : 'Henry',
            'stasiun awal' : 'Stasiun Gubeng',
            'waktu keberangkatan' : '16:15',
            'stasiun tujuan' : 'Stasiun Sidoarjo',
            'waktu kedatangan' : '18:30',
            'gerbong' : '2',
            'posisi duduk' : '5B'
        }
    }


user_input_menu = 0
    
def display_main_menu():
    global user_input_menu
    user_input_menu = int(
input('''
1. Cek data pengguna
2. Cek barang bawaan pengguna
3. Buka pintu masuk
4. Keluar
'''))

def check_user_data():
    user = grab_user_ticket()
    if user:
        print('Kode tiket : ', user['kode tiket'])
        print('Nama : ', user['nama'])
        print('Stasiun awal : ', user['stasiun awal'], '/', user['waktu keberangkatan'])
        print('Stasiun tujuan : ', user['stasiun tujuan'], '/', user['waktu kedatangan'])
        print('Gerbong : ', user['gerbong'])
        print('Posisi duduk: ', user['posisi duduk'])
        print('\n')
        
        check_actual_user_data(user['kode tiket'])
    else:
        print('Penumpang tidak valid!')
    
def grab_user_ticket():
    global current_user
    current_user += 1
    
    if current_user == len(users) + 1:
        print('Antrian penumpang sudah selesai')
        input('Lanjutkan => ')
        return {}
    else:
        return users[current_user]

def check_actual_user_data(user_ticket):
    user_input_confirmation = str(input('Cek data aktual ? [y/n] '))
    if user_input_confirmation == 'y':
        actual_user = {}
        for key in real_user:
            user = real_user[key]
            if user['kode tiket'] == user_ticket:
                actual_user = user
                break
        
        if actual_user:
            print('============================================')
            print('Kode tiket : ', actual_user['kode tiket'])
            
            is_found_not_match = False
            if users[current_user]['nama'] != actual_user['nama']:
                is_found_not_match = True
                print('\033[31mKode tiket : ', actual_user['kode tiket'], '\033[0m')
            else:
                print('Nama : ', actual_user['nama'])
            
            if users[current_user]['stasiun awal'] != actual_user['stasiun awal']:
                is_found_not_match = True
                print('\033[31mStasiun awal : ', actual_user['stasiun awal'], '/', actual_user['waktu keberangkatan'], '\033[0m')
            else:
                print('Stasiun awal : ', actual_user['stasiun awal'], '/', actual_user['waktu keberangkatan'])
                
            if users[current_user]['stasiun tujuan'] != actual_user['stasiun tujuan']:
                is_found_not_match = True
                print('\033[31mStasiun tujuan : ', actual_user['stasiun tujuan'], '/', actual_user['waktu kedatangan'], '\033[0m')
            else:
                print('Stasiun tujuan : ', actual_user['stasiun tujuan'], '/', actual_user['waktu kedatangan'])
                
            if users[current_user]['gerbong'] != actual_user['gerbong']:
                is_found_not_match = True
                print('\033[31mGerbong : ', actual_user['gerbong'], '\033[0m')
            else:
                print('Gerbong : ', actual_user['gerbong'])
            
            if users[current_user]['posisi duduk'] != actual_user['posisi duduk']:
                is_found_not_match = True
                print('\033[31mPosisi duduk: ', actual_user['posisi duduk'], '\033[0m')
            else:
                print('Posisi duduk: ', actual_user['posisi duduk'])
                
            print('\n')
            
            if not is_found_not_match:
                users[current_user]['isValid'] = True
            else:
                print('Data penumpang tidak valid!')
                
            input('Lanjutkan => ')
        else:
            print('Data pengguna tidak ditemukan!')
    
def check_user_stuffs():
    stuffs = investigate_user_stuffs()
    if stuffs:
        for key in stuffs:
            stuff = stuffs[key]
            print('Nama barang: ', stuff['nama'])
            print('Berat: ', stuff['berat'], 'kg')
            print('Ukuran: p=', stuff['ukuran']['panjang'], 'cm, l=', stuff['ukuran']['lebar'], 'cm, t=', stuff['ukuran']['tinggi'], 'cm')
            print('-----------------------------------------')
        input('Lanjutkan => ')
        calculate_user_fine(stuffs)
        input('Lanjutkan => ')
    else: 
        print('Penumpang tidak membawa barang bawaan apapun')
    
def investigate_user_stuffs():
    global current_user
    return users[current_user]['barang']

def calculate_user_fine(stuffs):
    print('Menghitung denda yang didapat')
    total_fine = 0
    for key in stuffs:
        stuff = stuffs[key]
        volume = stuff['ukuran']['panjang'] * stuff['ukuran']['lebar'] * stuff['ukuran']['tinggi']
        weight = stuff['berat']
        
        if volume > 30000:
            total_fine += volume % 30000 / 5000 * 10000
        
        if weight > 5:
            total_fine += weight % 5 * 5000
    
    users[current_user] = total_fine
    print('Penumpang akan dikenakan denda sebesar Rp ', locale.currency(total_fine, grouping=True))

def open_departure_gate():
    print('============================================')
    print('Gate opened!')
    print('============================================')
    for key in users:
        user = users[key]
        if user['isValid'] == True:
            print(user['nama'], ' masuk ke peron')
            time.sleep(0.5)
    
    print('\n')
    input('Lanjutkan => ')

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def main():
    initialize_data()
    display_main_menu()
    
    while user_input_menu < 5 and user_input_menu > 0:
        clear_terminal()
        if user_input_menu == 1:
            check_user_data()
        elif user_input_menu == 2:
            check_user_stuffs()
        elif user_input_menu == 3:
            open_departure_gate()    
        elif user_input_menu == 4:
            exit()
        
        clear_terminal()
        display_main_menu()
    
if __name__ == '__main__':
    main()