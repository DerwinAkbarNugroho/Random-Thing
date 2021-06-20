import time

def perjumlahan(x, y):
    return x + y
def pengurangan(x, y):
    return x - y
def perkalian(x, y):
    return x * y
def pembagian(x, y):
    return x / y

print("Select operation.")
print("1.perjumlahan")
print("2.pengurangan")
print("3.perkalian")
print("4.pembagian")

while True:
    mode = input("Mau yang mana? (1/2/3/4): ")

    if mode in ('1', '2', '3', '4'):
        num1 = float(input("Angka pertama: "))
        num2 = float(input("Angka kedua: "))
        print('Maaf, baru bisa 2 angka')
        time.sleep(0.7)

        if mode == '1':
            print(num1, "+", num2, "=", perjumlahan(num1, num2))

        elif mode == '2':
            print(num1, "-", num2, "=", pengurangan(num1, num2))

        elif mode == '3':
            print(num1, "*", num2, "=", perkalian(num1, num2))

        elif mode == '4':
            print(num1, "/", num2, "=", pembagian(num1, num2))
        break
    else:
        print("Opsi tidak valid")
