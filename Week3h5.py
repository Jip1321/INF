def teken_bord(bord):
    print("    1   2   3 ")
    print("  -----------")
    print("A | " + bord[0] + " | " + bord[1] + " | " + bord[2])
    print("-------------")
    print("B | " + bord[3] + " | " + bord[4] + " | " + bord[5])
    print("-------------")
    print("C | " + bord[6] + " | " + bord[7] + " | " + bord[8])
    print("")

def winnaar(bord, speler):
    win = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # matrix rijen zijn de 'winmogelijkheden'1e rij leest af de horizontale, 2e == voor verticaal , 2e zijn voor diagonalen
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for voorwaarde in win:
        if bord[voorwaarde[0]] is speler and bord[voorwaarde[1]] is speler and bord[voorwaarde[2]] is speler:
            return True
    return False


bord = [" "] * 9  
spelers = ["X", "O"]  
Speler1 = 0  

for beurt in range(9):  
    teken_bord(bord)
    
    while True:
        rij = input(f"Speler {spelers[Speler1]} kies uit verticale rij a, b of c: ")
        kolom = int(input(f"Speler {spelers[Speler1]} kies uit horizontale rij 1, 2 of 3: ")) - 1 
        
        if rij == "A":
            index = kolom
        elif rij == "B":
            index = 3 + kolom
        elif rij == "C":
            index = 6 + kolom
        else:
            print("Kies a, b of c")
            continue

        if 0 <= kolom < 3:  
            if bord[index] == " ":  
                bord[index] = spelers[Speler1]  
                break  
            else:
                print("dit vak is bezet")
        else:
            print("invalide nummer")

    if winnaar(bord, spelers[Speler1]):
        teken_bord(bord)
        print(f"{spelers[Speler1]} wint")
        break
    
    Speler1 = 1 - Speler1  # Wissel van beurt (x == 0, O == 1. Lijn 24 verwijst dat x als eerst begint)

teken_bord(bord)
if not winnaar(bord, spelers[0]) and not winnaar(bord, spelers[1]):
    print("Remise")
