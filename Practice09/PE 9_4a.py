import csv
with open ('artikel.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('Wat is het artikelnummer: ')
        if artikelnummer == '':
            break
        artikelcode =
        naam =
        voorraard =
        prijs =
        writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
