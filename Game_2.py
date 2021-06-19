import time
import random

print('Oke, mari kita mulai...')
a = int(input('Berapa kesempatan  yang ingin dimiliki? '))
to_range = int(input('Radius angka 1 hingga... '))
time.sleep(0.5)
print('Baik, aku memikirkan angka dari 1 sampai', to_range, '. Coba tebak angka berapa itu')
time.sleep(0.3)
print('Kau memiliki', a, 'kesempatan untuk menebak')
tebakan = 0
pemain = False
while pemain == False:
    nomer = random.randint(1, to_range)
    
    while tebakan < a:
        pemain = int(input())
        tebakan += 1
        
        if pemain < nomer:
            print('Angkamu masih kekecilan')
        elif pemain > nomer:
            print('Angkamu kebesaran')
        else:
            print('Selamat, kamu menebak angka yang benar hanya dengan', tebakan, 'tebakan')
            break
        
        time.sleep(0.3)
        
        if tebakan < a-1:
            print('Kesempatan tinggal', a - tebakan, 'lagi')
        elif tebakan == a-1:
            print('Kesempatan terakhir, ayo')
        else:
            print('Welp, salah')

    if pemain != nomer:
        print('Kesempatan habis, angka yang betul adalah', nomer)
    restart = input('Apa mau mencoba lagi? ')
    if restart == 'Iya':
        pemain=False
        tebakan = 0
        print('Baik, angka baru, 1 sampai', to_range, 'angka berapa?')
    elif restart == 'Tidak':
        print('Oke, baiklah')
    else:
        print('Cek ejaan')

print('Terimakasih sudah bermain...')