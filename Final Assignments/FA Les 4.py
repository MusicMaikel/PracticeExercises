def standaardprijs(afstandKM):
    bedrag = 0.0
    if afstandKM > 50:
        bedrag = afstandKM * 0.60 + 15
    elif afstandKM > 0:
        bedrag = afstandKM * 0.80
    else:
        bedrag = 0
    return (bedrag)

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if (leeftijd < 12 or leeftijd >= 65) and weekendrit == False:
        kortingsprijs = prijs - (prijs/100*30)
        return (round(kortingsprijs, 2))
    elif (leeftijd < 12 or leeftijd >= 65) and weekendrit == True:
        kortingsprijs = prijs - (prijs / 100 * 35)
        return (round(kortingsprijs, 2))
    elif (leeftijd >= 12 or leeftijd < 65) and weekendrit == True:
        kortingsprijs = prijs - (prijs / 100 * 40)
        return (round(kortingsprijs, 2))
    else:
        kortingsprijs = prijs
        return (round(kortingsprijs,2))

afstandKM = eval(input('Hoeveel kilometer reist u? '))
leeftijd = eval(input('Wat is uw leeftijd? '))
input_weekendrit = input('Reist u in het weekend? (True or False) ')

if input_weekendrit == 'True' or input_weekendrit == 'true':  # hier maak ik een boolean van de invoer van weeekend rit
            weekendrit = True
elif input_weekendrit == 'False' or input_weekendrit == 'false':
            weekendrit = False
else:
    print("u heeft geen geldige waarde ingevuld bij weekendrit")

print('Uw kaartje kost ' + str(ritprijs(leeftijd, weekendrit, afstandKM)) + ' euro')

print('Afstanden onder 50 kilometer:')
print(ritprijs(64, False, 10))
print(ritprijs(11, False, 10))
print(ritprijs(12, False, 10))
print(ritprijs(65, False, 10))
print(ritprijs(11, True, 10))
print(ritprijs(12, True, 10))
print(ritprijs(64, True, 10))
print(ritprijs(65, True, 10))

print('Afstanden boven 50 kilometer:')
print(ritprijs(64, False, 60))
print(ritprijs(11, False, 60))
print(ritprijs(12, False, 60))
print(ritprijs(65, False, 60))
print(ritprijs(11, True, 60))
print(ritprijs(12, True, 60))
print(ritprijs(64, True, 60))
print(ritprijs(65, True, 60))

print('Afstanden onder 0 kilometer:')
print(ritprijs(64, False, -10))
print(ritprijs(11, False, -10))
print(ritprijs(12, False, -10))
print(ritprijs(65, False, -10))
print(ritprijs(11, True, -10))
print(ritprijs(12, True, -10))
print(ritprijs(64, True, -10))
print(ritprijs(65, True, -10))
