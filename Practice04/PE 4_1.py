def som():
    som = getal1 + getal2 + getal3
    return som

getal1 = eval(input('Geef het eerste getal: '))
getal2 = eval(input('Geef het tweede getal: '))
getal3 = eval(input('Geef het derde getal: '))

print('De som van de 3 getallen is ' + str(som()))
