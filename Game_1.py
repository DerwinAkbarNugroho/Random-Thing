import time
from random import randint
#Ndak tau napa pengen nyoba
a = ['Kertas', 'Batu', 'Gunting']
bot = a[randint(0,2)]
pemain = False

while pemain == False:
    pemain = input('Gunting, Batu, Kertas? Pastikan penulisan diawalai huruf kapital ')
    time.sleep(0.7)
    if pemain == bot:
        print(pemain, 'lawan', bot, ', seri')
    elif pemain == 'Kertas':
        if bot == 'Batu':
            print(pemain, 'lawan', bot, ', selamat anda MENANG!!!!1!111')
        else:
            print(pemain, 'lawan', bot, ', kalah')
    elif pemain == 'Gunting':
        if bot == 'Kertas':
            print(pemain, 'lawan', bot, ', selamat anda menang')
        else:
            print(pemain, 'lawan', bot, ', kalah....')
    elif pemain == 'Batu':
        if bot == 'Gunting':
            print(pemain, 'lawan', bot, ', selamat anda menang')
        else:
            print(pemain, 'lawan', bot, ', kalah...')
    else:
        print('Coba cek penulisan anda, pastikan diawali dengan huruf kapital')
    time.sleep(0.4)
    c = input('Mau main lagi? Iya atau Tidak? ')
    time.sleep(0.5)
    if c == 'Iya':
        pemain = False
        bot = a[randint(0,2)]
    elif c == 'Tidak':
        print('Terima kasih sudah bermain')
    else:
        print('Coba cek penulisan dan kapital anda')