# Sistem masuk kereta api

current_user = 0

def initialize_data():
    global users
    users = {
        1 : {
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
                        'lebar' : 50,
                        'tinggi' : 200
                    }
                },
                2 : {
                    'nama' : 'koper',
                    'berat' : 7,
                    'ukuran' : {
                        'panjang' : 50,
                        'lebar' : 30,
                        'tinggi' : 100
                    }
                }
            }
        },
        2 : {
            'kode tiket' : '98YB87',
            'nama' : 'Angel',
            'stasiun awal' : 'Stasiun Gubeng',
            'waktu keberangkatan' : '16:21',
            'stasiun tujuan' : 'Stasiun Blitar',
            'waktu kedatangan' : '22:35',
            'gerbong' : '1',
            'posisi duduk' : '11D',
            'barang' : {}
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
    return users[current_user]

def check_actual_user_data(user_ticket):
    user_input_confirmation = str(input('Check data aktual ? [y/n] '))
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
            print('Nama : ', actual_user['nama'])
            print('Stasiun awal : ', actual_user['stasiun awal'], '/', actual_user['waktu keberangkatan'])
            print('Stasiun tujuan : ', actual_user['stasiun tujuan'], '/', actual_user['waktu kedatangan'])
            print('Gerbong : ', actual_user['gerbong'])
            print('Posisi duduk: ', actual_user['posisi duduk'])
            print('\n')
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
    else: 
        print('Penumpang tidak membawa barang bawaan apapun')
    
def investigate_user_stuffs():
    global current_user
    return users[current_user]['barang']



# EXECUTION AREA!
initialize_data()
display_main_menu()


while user_input_menu < 5 and user_input_menu > 0:
    if user_input_menu == 1:
        check_user_data()
    elif user_input_menu == 2:
        check_user_stuffs()
    
    display_main_menu()
