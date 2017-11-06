som = 0
aantal = 0

while True:
    getal = eval(input('Geef getal: '))
    if getal == 0:
        break
    else:
        som = som + getal
        aantal = aantal + 1

print(som)
print(aantal)
