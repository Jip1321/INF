
Week 4.1
Straks gaan we werken met tekst-bestanden. Je werkt namelijk meestal niet met losse getallen, letters of woorden, maar met een hele bak aan data. Denk aan meetwaarden of lappen tekst, of als je een app bouwt: aan alle gebruikers of posts.

Werken met tekst
We gaan aan de slag met strings: stukken tekst. Het eerste voorbeeld was "Hello world". Maar uiteraard zijn er ook veel langere stukken tekst. De standaard opvultekst die eigenlijk nergens op slaat is Lorem ipsum:

lorem = """Lorem ipsum dolor sit amet. Non itaque architecto qui expedita voluptas eum natus totam. Est mollitia voluptatem aut deleniti labore hic dolore vero aut suscipit vitae aut animi officiis aut possimus nobis. Rem dignissimos repellat id internos quis et voluptatem cupiditate non rerum nulla qui tenetur quaerat et officiis molestiae.
Et dolores temporibus a voluptatum autem ut autem impedit. Eum iste assumenda in reprehenderit consequatur est minima iusto aut quod perferendis aut dolorum culpa.
Vel atque dicta est exercitationem recusandae et dolor voluptatibus. Ea alias placeat non sint molestias est amet dolores  adipisci sunt et quis veniam et voluptatibus pariatur non voluptas quia."""
Note

Je hebt een driedubbele apostrof nodig als er Enters in je tekst staan - zoals bij de tekst hierboven.

Opdracht 4.1
Je kunt de lengte van een string opvragen: Python telt dan hoeveel karakters (letters / spaties / cijfers / symbolen) er in je string zitten.

print(len(lorem))       # lorem is 692 karakters lang
Tip

len() is een ingebouwde functie in Python: net als de functies die je zelf hebt gemaakt in het vorige hoofdstuk, kun je hier een argument gebruiken: namelijk het 'item' waarvan je de lengte wilt weten.

Er zijn een aantal handige dingen die je kunt doen met strings. Een daarvan is het splitsen op bepaalde karakters:

gesplitst = lorem.split(' ')
De tekst wordt gesplitst op het karakter ' ': een spatie.

Opdracht 4.2
Opdracht 4.3
Een ander geintje is replace():

vervangen = lorem.replace('o', '0') # vervang alle letters o door het cijfer 0
vervangen2 = lorem.replace(' ', '') # vervang alle spaties door niets (verwijder dus alle spaties)
De eerste regel laat zien hoe je losse karakters kunt vervangen. De tweede regel is eigenlijk een soort verwijderen: we vervangen de spatie door een leeg karakter.

Tip: achter .replace() kun je gewoon nog een keer .replace() zetten om ook een ander karakter te vervangen.

Opdracht 4.4
Je kunt ook stukken tekst 'aan elkaar lijmen'. Een stukje terug werd lorem gesplitst op de spaties. Je kunt dat vervolgens weer op deze manier weer een normale tekst maken:

gelijmd = ' '.join(gesplitst)
Alle elementen in gesplitst worden gejoined met een spatie (' ').

Terug naar de schildpad
Na een poos bezig geweest te zijn met boter-kaas-en-eieren en teksten, gaan we nog even terug naar het tekenen met de schildpad. We hebben meer dingen geleerd waardoor het makkelijker wordt om figuurtjes te tekenen.

Importeren (eerste regel van je script):

import turtle
Important

Wanneer je turtle in een script wilt gebruiken, moet je altijd aan het einde van je script zetten:

turtle.mainloop()
Dit is dus altijd de laatste regel van je script

De basisomgeving
Werken met turtle is eigenlijk tekenen met een pen op papier. Met de volgende regel komen we aan 'papier':

s = turtle.getscreen()
Het papier zit opgeslagen onder de variabele s van screen. Let op: er opent een extra scherm (in de achtergrond).

Met de volgende regel komen we aan een pen:

t = turtle.Turtle()
De pen zit nu opgeslagen onder de variabele t van turtle. Nu kunnen we gaan tekenen!

Overzicht van basis-tekenfuncties
Een lijstje van de bekende teken-commando's:

t.forward(100)  # 100 units vooruit
t.forward(-25)  # 25 units achteruit
t.backward(50)  # 50 units achteruit
t.left(90)      # 90 graden naar links draaien
t.left(-45)     # 45 graden naar rechts draaien
t.right(180)    # 180 graden naar rechts draaien
Makkelijke afkortingen:

t.fd()
t.bk()
t.lt()
t.rt()
Als je fouten hebt gemaakt kun je de volgende commando's gebruiken:

t.undo()        # laatste actie ongedaan maken
t.clear()       # alle strepen verwijderen
t.reset()       # helemaal opnieuw beginnen
Om naar een specifieke plek op het scherm te gaan, zijn de volgende functies beschikbaar:

t.goto(x, y)        # ga naar het punt (x, y)
t.goto(-50, 10)     # ga naar het punt (-50, 10)
t.home()            # ga naar het punt (0, 0)
Zolang je pen op het papier staat, wordt er ook een lijn naar die plek getekend. Als je wilt voorkomen dat er een lijn komt te staan, kun je de pen optillen en later weer neerzetten:

t.up()
t.down()
En dan is er nog een verzameling aan (minder) handige functies:

t.position()        # huidige (x, y)-coordinaten weergeven
t.pos()             # korte alias van .position()
t.hideturtle()      # turtle onzichtbaar maken
t.showturtle()      # turtle zichtbaar maken
t.stamp()           # een stempel op de huidige plek van de turtle
En een aantal verschillende 'skins' voor je schildpad:

t.shape("turtle")
t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")
Een punt maak je zo:

t.dot(radius, color)
t.dot(10)           # een punt met straal 10
t.dot(20, "blue")   # een blauwe punt met straal 20
t.dot(5, "#15F204") # een (hexadecimaal) groene punt met straal 5
Voor een cirkel zijn er de volgende opties:

t.circle(radius, extent, steps)
t.circle(50)                # cirkel met r = 50
t.circle(30.5, 180)         # halve cirkel met r = 30.5
Een paar nieuwe commando's
Je kunt ook achtergrondkleuren instellen:

s.bgcolor(color)   # de achtergrondkleur van het papier instellen
s.bgcolor("red")
s.bgcolor("green")
s.bgcolor("magenta")
Voor het wijzigen van de lijndikte kan de pensize aangepast worden:

t.pensize(2)            # default is 1
Om de penkleur te wijzigen, kan het volgende gebruikt worden:

t.pencolor('brown')     # string
t.pencolor(0.8, 0, 0.2) # RGB 0..1
t.pencolor(0, 100, 255) # RGB 0..255
t.pencolor('##8F438F')  # hexadecimaal
t.pencolor()            # geeft de huidige kleur weer
Naast lijnen kleuren is het ook mogelijk om vlakken te vullen met een kleur. De vulkleur stel je in op dezelfde manier als de penkleur hierboven:

t.fillcolor(color)  # string, RGB 0..1, RGB 0..255, hex
Een vlak vullen moet je specifiek zelf doen door gebruik te maken van begin_fill() en end_fill()!

t.begin_fill()  	# alles wat tussen begin_fill en end_fill staat, wordt opgevuld
t.circle(50)
t.end_fill()        # de cirkel vullen met een kleur
Maak een van onderstaande opdrachten:

Opdracht 4.5
Maak een smiley: een grote cirkel, met twee dots voor ogen. De mond moet een deel van een cirkel zijn.

Opdracht 4.6
Maak een schietschijf die bestaat uit uit vier schijven: van buiten naar binnen een zwarte, blauwe, rode en gele. Er zijn meerdere manieren mogelijk om dit te tekenen.

Eventueel kun je met t.stamp() een paar random plekken markeren waar je 'geschoten' hebt.

turtle en loops
Waar er tot nu toe veel handwerk nodig was om iets moois te maken, kunnen we uiteraard ook hier weer automatisering toepassen.

Vergelijk de volgende twee methoden om een vierkant te maken:

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
of:

for i in range(4):  # i = 0, 1, 2, 3
    t.fd(100)
    t.rt(90)
Of in een keer een paar cirkels van verschillend formaat:

for i in range(10, 50, 10): # i = 10, 20, 30, 40
    t.circle(i)             # cirkel met straal i
Een ander leuk voorbeeld:

for i in range(10, 250, 5): # i = 10, 15, 20 .. 240, 245
    t.fd(i)
    t.lt(90)
Herinnering: als je turtle in een script gebruikt, moet je altijd aan het einde van je script zetten:

turtle.mainloop()
Opdracht 4.7
Maak met behulp van een aantal for-loops een driehoek, vierhoek, zeshoek en achthoek. Hint: als je n hoeken gebruikt, moet je de turtle met 360/n graden draaien.

Opdracht 4.8
Maak een vijfpuntige ster uit één lijn door een for-loop te gebruiken.

Tip: de schildpad moet twee keer helemaal rond, dus 720 graden. Bereken zelf welke hoek je dan moet maken voor elke punt.

Zolang als...
De for-loop doet de code die je erbij zet precies x aantal keren. Maar soms weet je van tevoren niet hoe vaak iets moet gebeuren. Of wil je wachten tot een bepaald moment. Bijvoorbeeld: zolang als de docent aan het woord is, ben ik stil. Of zolang als we nog niet gaan eten, lees ik nog in m'n boek of ga ik nog een potje gamen. De Engelse vertaling hiervan is uiteraard while. We gaan dit gebruiken om zometeen een bestand in te lezen: zolang als het bestand nog niet 'uit' is, lezen we er elke keer nog een regel uit. Totdat we aan het einde van het bestand zijn gekomen.

Eerst een voorbeeld en tweetal oefeningen:

x = 0           # startwaarde 0
while x < 10:   # zolang x kleiner is dan 10...
    print(x)    # print de waarde van x
    x = x + 1   # en tel 1 op bij x
Opdracht 4.9
Test de code hierboven uit. Als je goed kijkt naar de uitvoer, zie je dat het getal 10 helaas toch niet geprint wordt. Vind twee (of met een beetje creativiteit drie of vier) manieren om alle getallen van 0 tot en met 10 te printen waarbij je gebruik maakt van (een variant van) bovenstaande while-loop.

Opdracht 4.10
In hoofdstuk 2 heb je regelmatig dobbelstenen gegooid. Als je (Kolonisten van) Catan speelt, heb je twee dobbelstenen. Als je die gooit en je gooit 7, dan heb je regelmatig pech. De ene keer gebeurt dat heel snel, de andere keer kan het lang duren voordat er 7 wordt gegooid. Schrijf een klein programmaatje dat elke keer opnieuw twee dobbelstenen gooit, totdat ze samen optellen tot 7.

Het opstapje voor deze opdracht:

import random

dice = [_]
throw1 = 0  # nog geen dobbelsteen gegooid
throw2 = 0  # nog geen dobbelsteen gegooid

while _:    # zolang beide geworpen dobbelstenen samen niet optellen tot 7...
    throw1 = random.choice(_)
    throw2 = _
    print("Je hebt gegooid:", _)    # print de optelling

print("Einde van het programma")
Een bestand inlezen
Vanaf nu tot en met het einde van het blok gaan we aan de slag om een tekenprogramma te schrijven waarbij we turtle gebruiken. Tekenprogramma's zoals Adobe Illustrator werken eigenlijk altijd met vectortekeningen, of simpeler gezegd lijntekeningen (in tegenstelling tot pixels in een foto). Het voordeel van lijntekeningen is dat ze eindeloos accuraat zijn en niet bestaan uit pixels.
Bij turtle maken we ook gebruik van zulke lijnstukken in tegenstelling tot pixels. Goed, je scherm heeft alleen pixels dus uiteindelijk ziet het er altijd uit als pixels. Maar je hoeft gelukkig niet met de hand pixels te kleuren, je zegt alleen dat je een 'lijnstuk' wilt tekenen (bijvoorbeeld: forward(100)).
Lijntekeningen als .svg zijn eigenlijk een lange rij commando's die vertellen welke lijnstukken er getekend zijn. Als jij dat bestand opent hoef je gelukkig niet zelf al die lijnstukken te tekenen: dat wordt automatisch voor je gedaan. In Python gaan we dat ook doen voor de turtle! Daarom gaan we kijken hoe Python een bestand kan inlezen, waarna we alle commando's automatisch laten uitvoeren.

# open het bestand 'tekening.txt' in 'r'(ead) modus
file = open("tekening.txt", "r")

# ..iets doen met de inhoud van het bestand

# sluit het bestand
file.close()
Warning

De laatste regel is net zo belangrijk als de eerste: als je een bestand niet sluit gaat Windows vaak raar doen. Hij denkt dan namelijk nog dat het bestand geopend is met een rij errors tot gevolg (of stevig vastlopen).

Opdracht 4.11
Maak in je map met Python bestanden een nieuw bestand met de naam tekening.txt. Op GitHub staat een bestand met dezelfde naam bij de lesstof. Kopieer de inhoud van dat bestand naar je eigen computer. Test vervolgens bovenstaand stukje script. Je kunt het beste in een leeg script (nieuw Python bestand) beginnen in dezelfde map als het tekstbestand.

Als je geen error krijgt bij het uitvoeren van bovenstaande code, dan is alles in orde. Als je wel een error krijgt bij bovenstaande code, doe dan het volgende: ga in Visual Studio Code naar File > Open Folder en open dan specifiek de map waarin je Python script én tekstbestand zijn opgeslagen (ze moeten in dezelfde map staan).

We kunnen alle regels in het bestand uitlezen en printen:

# .. open het bestand zoals eerder
while regel := file.readline():
    print(regel)
# .. sluit het bestand zoals eerder
Note

Je ziet een vrij gekke operator staan: :=. Deze hoef je niet te kennen, maar hij heet de walrus-operator ("because the := syntax resembles the eyes and tusks of a walrus lying on its side").
Wat deze operator doet, is het volgende: regel krijgt de waarde van file.readline() (ofwel: de volgende regel uit het bestand), maar tegelijkertijd wordt ook gecheckt of er nog wel een regel is in het bestand. Je kunt het dus als volgt lezen:
"Zolang er nog een line in het bestand is, sla je deze line op in regel en voer je de volgende code uit: ..."

Opdracht 4.12
Voer bovenstaande code uit en check of de regels goed geprint worden!

De eerste letter van elke regel is het commando dat door je schildpad uitgevoerd moet worden. De mogelijke opties zijn:

Afkorting	Commando
f	forward
b	backward
l	left
r	right
o	dot
s	begin_fill
e	end_fill
p	pencolor
i	fillcolor
c	circle
u	up
d	down
g	goto
Match-case
Python heeft ingebouwd een mooi trucje om met opties overweg te kunnen: de match-case constructie.

stoplicht = "groen"

match stoplicht:
    case "rood":
        print("Stilstaan")
    case "oranje":
        print("Afremmen")
    case "groen":
        print("Rijden")
    case _:
        print("Dat kan niet")
In dit voorbeeld gaan we een stuk code matchen op de variabele stoplicht. In het geval (in case) dat de waarde "rood" is, dan print de code dat je moet stilstaan; bij "oranje" dat je moet afremmen, en bij "groen" dat je mag rijden. In alle andere gevallen (_) wordt geprint dat een stoplicht die kleur niet kan hebben.

Opdracht 4.13
Maak een functie uitvoeren, met één argument: regel. Zet de volgende twee regels bovenaan in de functie:

commando = regel[0]                 # de eerste letter van de regel
argument = regel[1:].strip('\n')    # de rest, en strip de Enter
Bouw in de functie een match-case constructie. Match op commando, met een case voor alle opties in de tabel met commando's. Voor nu print je in elke case het commando dat straks uitgevoerd moet worden. Vergeet niet de laatste case: voor alle overige opties.

Een opstapje:

def _(_):
    commando = _
    argument = _
    match _:
        case _:
            print(_)
Let goed op alle tabs/inspringingen.

Een paar cases krijg je cadeau - de andere schrijf je zometeen zelf.

case 'i':
    t.fillcolor(argument)
case 'c':
    (rad, deg) = argument.split(',')
    t.circle(float(rad), float(deg))
case 'u':
    t.up()
case 'd':
    t.down()
case 'g':
    (x, y) = argument.split(',')
    t.goto(float(x), float(y))
Opdracht 4.14
Kopieer bovenstaande cases, en maak de andere cases compleet! Stel dat een regel "f100" is, dan is het commando "f" en het argument "100". Je turtle moet dan met 100 vooruit.

Tip: als het argument een getal moet zijn, moet je het nog omzetten van een string naar een float (kommagetal). Dat kan met float(argument).

Test je functie met het volgende stukje code:

import turtle
t = turtle.Turtle()

# zet hier jouw functie uitvoeren(regel) neer

uitvoeren("f100")
uitvoeren("l90")
uitvoeren("c200,180")
uitvoeren("r270")
uitvoeren("b-100")

turtle.mainloop()
Slotopdracht ⭐
Op GitHub staat een bestand genaamd tekening.txt. Maak in de map met je script een bestand met dezelfde naam. Kopieer de inhoud van het GitHub bestand en sla het op in je eigen bestand.

Open vervolgens in het script het bestand, en voer voor elke regel in het bestand de functie uitvoeren uit. Hiervoor kun je terugkijken naar een paar opdrachten terug: gebruik een for-loop: voor elke regel in het bestand moet je jouw functie uitvoeren met die regel.

Als je alles goed hebt gedaan krijg je een plaatje in beeld. Lukt het niet? Kijk dan of je een error ziet die je begrijpt. Werkt je script / zie je een goed plaatje? Ga dan door naar tekening2.txt.

Tip: stel vóór het tekenen de snelheid van je turtle in op maximaal: t.speed(10). Of als je helemaal geen animatie wilt: t.speed(0). Anders ben je (zeker met het laatste bestand) lang aan het wachten...

dit staat in het bestand tekening.txt

u
l90
f200
d
r90
ipink
s
c10,180
c25,110
l50
c60,45
c20,170
r24
f30
l10
c30,110
f20
l40
c90,70
c30,150
r30
f15
c80,90
l15
f45
r165
f20
l155
c150,80
l50
c150,90
e
l150
c-90,70
l20
c75,105
l-261.0
c80,98
c-90,40
l180
c90,40
c-80,98
l-323.0
f30
l90
f25
l45
igreen
s
c-80,90
r90
c-80,90
e
r135
f60
l180
f85
l90
f80
r90
r45
igreen
s
c80,90
l90
c80,90
e
l135
f60
l180
f60
r90
c200,60
