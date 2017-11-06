def ticker():
    infile = open('ticker.txt', 'r')
    regels = infile.readlines()
    infile.close()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict

tickerbestand = ticker()

bedrijfsnaam = input('Wat is de bedrijfsnaam: ')
for bedrijf in tickerbestand:
    if bedrijf == bedrijfsnaam:
        print('Ticker symbool: {}'.format(tickerbestand[bedrijf]))

tickercode = input('Schrijf Ticker symbool: ')
for bedrijf in tickerbestand:
    if tickerbestand[bedrijf] == tickercode:
        print('Bedrijfsnaam is: {}'.format(bedrijf))

ticker()
print(ticker())
