import random, time

Buah = ['apel', 'jeruk', 'mangga', 'pisang', 'pir', 'kelapa', 'rambutan', 'durian', 'pepaya', 'anggur']
Sayuran = ['tomat', 'semangka', 'cabai', 'kacang panjang', 'bawang', 'melon', 'kangkung', 'wortel', 'bayam']
Kendaraan = ['mobil', 'motor', 'kapal', 'pesawat', 'kereta', 'sepeda', 'bis', 'truk', 'helikopter']
Makanan = ['nasi goreng', 'gudeg', 'bubur', 'roti', 'tempe', 'tahu', 'bakwan', 'mendoan', 'salad', 'mie goreng']
Minuman = ['susu', 'soda', 'kopi hitam', 'es dawet', 'kopi susu', 'teh tawar', 'jus', 'es mokacino']

Daftar_tebakan = []
tebakan = []
Status = True

print("Halo pemain, apakah anda siap memainkan Hangman?")
time.sleep(1)
print('Ada 5 kategori kata, buah, sayuran, kendaraan, makanan, dan minuman.')
time.sleep(0.7)
kategori = input('Tekan B untuk buah, S untuk sayuran, K untuk kendaraan, Ma untuk makanan, dan Mi untuk minuman, atau X untuk keluar ')
a = int(input('Kesempatan salah berapa kali? '))
while True:
    while True:
        if kategori == 'B':
            Kata = random.choice(Buah)
            break
        elif kategori == 'S':
            Kata = random.choice(Sayuran)
            break
        elif kategori == 'K':
            Kata = random.choice(Kendaraan)
            break
        elif kategori == 'Ma':
            kata = random.choice(Makanan)
            break
        elif kategori == 'Mi':
            kata = random.choice(Minuman)
            break
        else:
            kategori = input("Pilih huruf yang valid, B untuk buah, S untuk sayuran, K untuk kendaraan, Ma untuk makanan, Mi untuk minuman, dan X untuk keluar")

        if kategori == 'X':
            print("Baik,sampai jumpa lagi!")
            Status = False
            break

    if Status:
        Daftar_kata = list(Kata)
        Percobaan = (len(Kata) + a)

        def Yang_ketebak():
            print("Yang harus kau tebak adalah: " + ''.join(Daftar_tebakan))

        for n in Daftar_kata:
            Daftar_tebakan.append('_')
        Yang_ketebak()

        print("Kau memiliki:", Percobaan, 'x kesempatan menebak')

        while True:

            print("Silahkan menebak:")
            huruf = input()

            if huruf in tebakan:
                print("Sudah kau coba.")

            else:
                Percobaan -= 1
                tebakan.append(huruf)
                if huruf in Daftar_kata:
                    print("Betul!")
                    if Percobaan > 0:
                        print("Tinggal ", Percobaan, 'tebakan lagi!')
                    for i in range(len(Daftar_kata)):
                        if huruf == Daftar_kata[i]:
                            hurufIndex = i
                            Daftar_tebakan[hurufIndex] = huruf.upper()
                    Yang_ketebak()

                else:
                    print("Salah, coba huruf lain.")
                    if Percobaan > 0:
                        print("Tinggal ", Percobaan, 'tebakan lagi!')
                    Yang_ketebak()


            Menang = ''.join(Daftar_tebakan)
            if Menang.upper() == Kata.upper():
                print("Ketebak semua, selamat anda menang!!.")
                break
            elif Percobaan == 0:
                print("Kesempatan habis, anda kalah.")
                print("Katanya adalah: "+ Kata.upper())
                break

        Lanjut = input("Mau main lagi? Pencet Y jika mau, tekan selain itu untuk berhenti ")
        if Lanjut == 'Y':
            kategori = input("Masukkan kode kategori seperti diatas ")
            Daftar_tebakan = []
            tebakan = []
            Status = True
        else:
            print("Ok, terimakasih sudah bermain!")
            break
    else:
        break