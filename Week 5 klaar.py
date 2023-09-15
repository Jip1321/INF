from tkinter import *
from tkinter import messagebox

# je kunt in python canvas gebruiken via tkinter en vanuit daaruit is het mogelijk om hetzelfde te krijgen zoals je kunt in html5 wat we vorig jaar hebben geleerd
# voeg je hier buttons toe dan kan je berekeningen achter zetten en met de functie messagebox kan je meldingen laten zien op basis van de berekeningen



#functie voor waardes verwijderen
def reset_entry():
    Leeftijd.delete(0, 'end')
    Lengte.delete(0, 'end')
    Gewicht.delete(0, 'end')
#functie voor berekenen gebaseerd op de waardes in label
def calculate_bmi():
    kg = int(Gewicht.get())
    m = int(Lengte.get()) / 100

    # bereken Bmi
    bmi = kg / (m * m)
    bmi = round(bmi, 1)

    # Bmi melding
    bmi_index(bmi)
# zie documentatie voor message box https://docs.python.org/3/library/tkinter.messagebox.html
def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo(None, f'BMI = {bmi} Ondergewicht!')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo(None, f'BMI = {bmi} Normaal!')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo(None, f'BMI = {bmi} Overgewicht!')
    elif bmi >= 29.9:
        messagebox.showinfo(None, f'BMI = {bmi} Obesitas!')
    else:
        messagebox.showinfo(None, 'Er ging wat mis, Heb je alles wel ingevuld?!')

# canvas creeren
ws = Tk()
ws.title('BMI berekenen')
ws.geometry('400x400')
ws.config(bg='cyan')
# verlklaren van variable
var = IntVar()

# frame om canvas zodat mooier uitziet ( standaart is zwart uitlijn)
frame = Frame(ws, padx=10, pady=10)
frame.pack(expand=True)

# buttons en info ( is mogelijk om in docu na te lezen)
Label(frame, text="Vul je leeftijd in!").grid(row=1, column=1)
Leeftijd = Entry(frame)
Leeftijd.grid(row=1, column=2, pady=5)

Label(frame, text='Ben je Man of Vrouw?').grid(row=2, column=1)
frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(frame2, text='Man', variable=var, value=1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2, text='Vrouw', variable=var, value=2)
female_rb.pack(side=RIGHT)

Label(frame, text="Vul je hoogte in cm").grid(row=3, column=1)
Label(frame, text="Vul je Gewicht in kg").grid(row=4, column=1)

Lengte = Entry(frame)
Lengte.grid(row=3, column=2, pady=5)

Gewicht = Entry(frame)
Gewicht.grid(row=4, column=2, pady=5)

# interactie + berekening
frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

Button(frame3, text='Bereken', command=calculate_bmi).pack(side=LEFT)
Button(frame3, text='Reset', command=reset_entry).pack(side=LEFT)
Button(frame3, text='uitloggen', command=lambda: ws.destroy()).pack(side=RIGHT)

# ws = tk
ws.mainloop()
