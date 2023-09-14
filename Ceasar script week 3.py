
# functie waarbij caracter waarde word gedefinieerd, en aantal caracters in alfabet vastgesteld
def new_text(x, verschuiving):
    if x.isalpha():
        shifted = ord(x) - verschuiving

        if x.islower():
            if shifted < ord('a'):
                shifted += 26
        elif x.isupper():
            if shifted < ord('A'):
                shifted += 26

        return chr(shifted) # returns asci tabel waarde
    else:
        return x

# functie voor het x te "vertalen"
def decryptie(raadsel, verschuiving):
    result = ""

    for x in raadsel:
        result += new_text(x, verschuiving)

    return result

# functie wat code heet 
# code is in dit geval de zin die we vertalen door verschuiving te nemen 
# en dan de waarde die we boven hebben berekent terug te geven zodat de getal weer een letter is
def Code():
    raadsel = ("xofob qyxxk qsfo iye ez, xofob qyxxk vod iye nygx")
    verschuiving = int(10)
    return raadsel, verschuiving

# status machine waar alle waardes weer terug komen van de functies gemaakt
def main():
    raadsel, verschuiving = Code()
    deciphered_text = decryptie(raadsel, verschuiving)
    print("Deciphered x:", deciphered_text)

# vervolgens printen we de functie van waardes uit, hij print dus main (status machine) uit waar alle waardes instaan
if __name__ == "__main__":
    main()