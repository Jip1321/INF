
# while loop waarbij word gevraagd om nummer, <2 dan gaat hij niet doordoor, >2 continue
while True:
  
    zijde_input = input("hoeveel zijdes heeft uw dobbelsteen? (Vul een nummer boven 2): ")

# if statement zou hier ook kunnen 
# maar omdat ik hier alleen check voor een input hoger/lager dan 2 kan ik ook try/except gebruiken met de functieblock ValueError wat ingebouwd in python zit
# hierdoor kan het input alleen  maar een getal zijn alles wat niet kan is een Error
    try:
        zijde = int(zijde_input)
    except ValueError:
        print("Vul een getal A.U.B.")
        continue

# dobb met 1 zijde werkt niet
    if zijde < 1:
        print("een getal onder de 1 werkt niet...")
        break

 # for loop om aantal ogen van zijde te berekenen 
    ogen = 0


    for x in range(zijde + 1):
        ogen += x

 # dit gedeelte kan ook paralel in print worden gedaan maar staat zo netter vind ik( refeer naar code die joram uit h5f heeft waar hij dat deed)
   # aantal_ogen = int(ogen / 2)

    print(f"een dobbelsteen met {zijde} zijdes, Dan krijg je {ogen} stippen.")
