
# while loop waarbij word gevraagd om nummer, <2 dan gaat hij niet doordoor, >2 continue
#while True:
  
  #  zijde_input = input("hoeveel zijdes heeft uw dobbelsteen? (Vul een nummer boven 2): ")

# if statement zou hier ook kunnen 
# maar omdat ik hier alleen check voor een input hoger/lager dan 2 kan ik ook try/except gebruiken met de functieblock ValueError wat ingebouwd in python zit
# hierdoor kan het input alleen  maar een getal zijn alles wat niet kan is een Error
 #   try:
 #       zijde = int(zijde_input)
 #   except ValueError:
 #       print("Vul een getal A.U.B.")
  #      continue

# dobb met 1 zijde werkt niet
 #   if zijde < 1:
#        print("een getal onder de 1 werkt niet...")
 #       break

 # for loop om aantal ogen van zijde te berekenen 
 #   ogen = 0


 #   for x in range(zijde + 1):
 #       ogen += zijde

 # dit gedeelte kan ook paralel in print worden gedaan maar staat zo netter vind ik( refeer naar code die joram uit h5f heeft waar hij dat deed)
 #   aantal_ogen = int(ogen / 2)

#    print(f"een dobbelsteen met {zijde} zijdes, Dan krijg je {aantal_ogen} stippen.")



while True:
    zijde_input = input("Hoeveel zijdes heeft uw dobbelsteen? (Vul een nummer boven 2): ")

    try:
        zijde = int(zijde_input)
    except ValueError:
        print("Vul een getal A.U.B.")
        continue

    if zijde <= 1:
        print("Dobbelsteen met minder dan 2 zijdes kan niet")
        break
# ik ga ervan uit u dit bedoelde met (1+2+3) wat op bord stond, 
    ogen = sum(range(1, zijde+1)) 
# range(1,zijdes+1) betekend dat als je 5 invult dan gaat hij een rij maken met getallen oplopend tot 5( begint bij 1 en eindigt bij de input waarde) = [1+2+3+4+5] 
# vervolgens willen we aantal ogens weten daarvoor gebruiken we sum die het rij pakt en opteld, [1+2+3+4+5]=15 ogen 

    print(f"Een dobbelsteen met {zijde} zijdes heeft in totaal {ogen} ogen.")
