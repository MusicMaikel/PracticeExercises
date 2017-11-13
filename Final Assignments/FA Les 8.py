stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert','Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    beginstation = input('Geef beginstation: ')
    while beginstation not in stations:
        print('Deze trein komt niet langs de route, geef een andere.')
        beginstation = input('Geef beginstation: ')
    return beginstation

def inlezen_eindstation(stations, beginstations):
    eindstation = input('Geef einstation: ')
    while eindstation not in stations:
        print('Deze trein komt niet langs de route, geef een andere.')
        eindstation = input('Geef eindstation: ')
    while stations.index(eindstation) <= stations.index(beginstations):
        print('Deze trein komt niet langs de route, geef een andere.')
        eindstation = input('Geef beginstation: ')
    return eindstation

def omroepen_reis(station, beginstation, eindstation):
    nummerB = stations.index(beginstation) + 1
    nummerE = stations.index(eindstation) + 1
    print('Het beginstation {} is het {}e station in het traject.'.format(beginstation, nummerB))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindstation, nummerE))
    afstand = nummerE - nummerB
    print('De afstand tussen {} en {} is {} stations.'.format(nummerB, nummerE, afstand))
    prijs = 5 * afstand
    print('De prijs van de reis tussen {} en {} is {}.'.format(nummerB, nummerE, prijs))
    print('Je stapt in in {}.'.format(beginstation))
    for i in range (nummerB, nummerE - 1):
        print('- ' + stations[i])
    print('Je stapt uit in {}.'.format(eindstation))

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
