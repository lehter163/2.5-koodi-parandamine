print("vali programm") #sisetab snad 
print("1 - Kolmnurga kontroll")
print("2 - Hinde arvutamine")
print("3 - Pileti hind")
valik=float(input("Sisesta valik (1-3) =>")) #ksib milline programm on vaja 
if valik == 1 : #kui inimene kirjutab 1 sis on kolmnurga kontrol 
    print("Kolmnurga kontroll") #panesin "
    a=float(input("Sisesta 1. klje pikkus => ")) #kirjutasin float ja "()"
    b=float(input("Sisesta 2. klje pikkus => ")) #panesin kinni ()
    c=float(input("Sisesta 3. klje pikkus => "))
    if a <= 0 or b <= 0 or c <= 0:
        print("kitjutage ainult positivsed numbrid")
    else:
        if a+b>c or a+c>b or b+c>a: #kirjutasin ":"
            print("Kolmnurk on olemas")
            if a == b == c : #kirjutasin kaks =
                print("Kolmnurk on vrdklgne")
            else:
                if a == b or b == c:
                    print("Kolmnurk on vrdhaarne")
                else:
                    print("Kolmnurk on eriklgne") #panesin if uue ridele(10),9 ridel kirjutasin ":". 11 ridel ja 9 ridel panen TAB
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
                 print("kolmnurk on taisnurke")
            else:
                 print("kolmnurk ei ole taisnurk")
        else:
            print("Sellist kolmnurka ei ole olemas")
        print()
else:
    if valik == 2 : #kui inimene kirjutab 2 sis on Hinde arvutamine
        print("Hinde arvutamine")
        punktid=int(input("Sisesta punktide arv (0-100) => "))
        if punktid<0 and punktid>100:
            print("Vigane punktide arv")
        elif punktid>=50 and punktid<=74: #kirjutasin et ainult numbrid 50 ja 74 Vaiksem kuni 75 on hind 3
            print("Hinne: 3")
        elif punktid>=75 and punktid<=89: #kirjutasin et ainult numbrid 75 ja 89 Vaiksem kuni 90 on hind 34
            print("Hinne: 4")
        elif punktid>=90:
            print("Hinne: 5")
        else:
            print("Hinne: 2")
        print()
    else:
        if valik == 3:#kui inimene kirjutab 3 sis on pileti hind
            print("Pileti hind")
            vanus=int(input("Sisesta oma vanus => "))
            if vanus>0 and vanus<7:
                print("Pilet on tasuta")
            elif 7<=vanus<=18 or vanus>=65: #kirjitasin > esimesel nt(>=)
                print("Pileti hind on 3 ")
            else: #kirjutasin ":"
                print("Pileti hind on 6 ")
        else:
            print("Vigane valik! kirjutage ainult nimbrid 1-3")
