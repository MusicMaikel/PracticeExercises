def ToonAantalKluizenVrij():
    infile = open("kluizen.txt", "r")
    kluizendata = infile.readlines()
    aantalbezet = len(kluizendata)
    over = 12 - aantalbezet
    infile.close()
    print("Er zijn nog {} kluizen vrij.\n".format(over))

def NieuweKluis():
    infile = open("kluizen.txt", "r")
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    kluizen = infile.readlines()
    for kluis in kluizen:
        info = kluis.split(";")
        kluisnr = int(info[0])
        if kluisnr in lst:
            lst.remove(kluisnr)
        else:
            if kluisnr in lst:
                code = eval(input("Wat is de code die u wilt gebruiken?: "))
            else:
                print("Sorry, er is geen kluis meer vrij.")

def KluisOpenen():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is je kluisnummer: ')
    code = input('Wat is je code: ')
    gegevenscorrect = False
    for regel in kluizendata:
        GegevensVanEenKluis = regel.split(';')
        stringkluisnummer = GegevensVanEenKluis[0]
        kluiscode = GegevensVanEenKluis[1]
        if stringnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect:
        print('Correct.')
    else:
        print('Niet correct.')



print('1 - Ik wil weten hoeveel kluizen er nog vrij zijn.')
print('2 - Ik wil een nieuwe kluis.')
print('3 - Ik wil iets uit mijn kluis halen.')

keuze = eval(input('Geef keuze in de vorm van het nummer: '))

if keuze == 1:
    ToonAantalKluizenVrij()
elif keuze == 2:
    NieuweKluis()
elif keuze == 3:
    KluisOpenen()
else:
    print('Dat is geen cijfer uit het menu. Probeer het opnieuw')

