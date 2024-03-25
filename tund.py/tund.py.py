from MinuOmaMoodul import*
salasõnad=loe_failist["Parool.1"]
kasutajanimed=loe_failist["Kasutaja1"]
while True:
    print(Kasutajanimed)
    print(salasõnad)
    print("1-registeerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=input("Sisestage arv")
    if vastus == 1:
        print("Registeerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus == 2:
        print("Autoriseerimine")
        autoriseerimine(kasutajad,salasõna)
    elif vastus == 3 :
        print("Nimi  või parooli muutmine")
        vastus==int(input("Kas muudame nimi või parooli?"))
        if vastus == "nimi":
            kasutajanimed=muutmine(kasutajanimed)
        elif vastus == "parool":
            salasõma=muutmine(salasõna)
        elif vastus == "mõlemad":
            kasutajanimed=muutmine(kasutajanimed)
            salasõma=muutmine(salasõna)
    elif vastus == 4:
        print("Unustanud porooli taastamine")
    elif vastus == 5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
