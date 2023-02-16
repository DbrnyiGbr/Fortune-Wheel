import random
szavak = ["iskolapad", "zöld", "idős", "időeltérés", "külváros", "arcszörzet", "sivatag", "házasság", "aligátor", "négyszáz", "zápor", "hányinger", 'diák', 'tengeri', 'beteg', 'kilométer', 'szem', 'temetés', 'befejezi', 'munka']

def megjelenites(lista):
    for i in lista: print(i, end="")



ujjatek = True
while ujjatek:

    feladvany = []
    dummy = random.randint(0, len(szavak)-1)
    szo = szavak[dummy].upper()
    for i in szo: feladvany.append(i)
    #print(szo)

    kiir = []
    for i in range(len(szo)): kiir.append("_ ")
    megjelenites(kiir)

    nincs_benne = set()
    game = True
    while game:
        print('')

        betu = '12'
        while len(betu) != 1 or betu.isalpha() == False: betu = input('Irjon be egy betűt: ').upper()

        if betu not in feladvany: nincs_benne.add(betu + ' ')
        else:
            for i in range(len(feladvany)):
                if feladvany[i] == betu: kiir[i] = betu

        megjelenites(kiir)
        print('\t' *2, end='')
        megjelenites(nincs_benne)

        if kiir == feladvany: game = False

    print('\nNyertél!')

    ujjatek_kerdes = input('Új játék? [Igen (I)/Nem (N)]: ').lower()
    if ujjatek_kerdes == 'n': ujjatek = False