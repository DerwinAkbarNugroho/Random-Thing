Papan_maen =    {'7': ' ' , '8': ' ' , '9': ' ' ,
           
                '4': ' ' , '5': ' ' , '6': ' ' ,
           
                '1': ' ' , '2': ' ' , '3': ' ' }

Isinya = []

for key in Papan_maen:
    Isinya.append(key)


def printPapan(Papan):
    print(Papan['7'], '|', Papan['8'], '|', Papan['9'])
    
    print('-+-+-')
    
    print(Papan['4'], '|', Papan['5'], '|', Papan['6'])
    
    print('-+-+-')
    
    print(Papan['1'], '|', Papan['2'], '|', Papan['3'])

def game():

    Giliran = 'X'
    Babak = 0


    for i in range(10):
        printPapan(Papan_maen)
        print("Sekarang giliran", Giliran, '. Silahkan maen.')

        Gerakan = input()        

        if Papan_maen[Gerakan] == ' ':
            Papan_maen[Gerakan] = Giliran
            Babak += 1
        else:
            print("Sudah terisi, pindah kemana?")
            continue

        if Babak >= 5:
            if Papan_maen['7'] == Papan_maen['8'] == Papan_maen['9'] != ' ':
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")                
                break
            elif Papan_maen['4'] == Papan_maen['5'] == Papan_maen['6'] != ' ':
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break
            elif Papan_maen['1'] == Papan_maen['2'] == Papan_maen['3'] != ' ':
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break
            elif Papan_maen['1'] == Papan_maen['4'] == Papan_maen['7'] != ' ': 
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break
            elif Papan_maen['2'] == Papan_maen['5'] == Papan_maen['8'] != ' ': 
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break
            elif Papan_maen['3'] == Papan_maen['6'] == Papan_maen['9'] != ' ': 
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break 
            elif Papan_maen['7'] == Papan_maen['5'] == Papan_maen['3'] != ' ':
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break
            elif Papan_maen['1'] == Papan_maen['5'] == Papan_maen['9'] != ' ':
                printPapan(Papan_maen)
                print("\nGame Over.\n")                
                print(" **** " +Giliran, " Menang. ****")
                break 

            if Babak == 9:
                print("\nGame Over.\n")                
                print("Wadoo sepertinya seri \n")

        if Giliran == 'X':
            Giliran = 'O'
        else:
            Giliran = 'X'        
    
    restart = input("Mau maen lagi?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in Isinya:
            Papan_maen[key] = " "

        game()

if __name__ == "__main__":
    game()
print('konsep by : https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874')
