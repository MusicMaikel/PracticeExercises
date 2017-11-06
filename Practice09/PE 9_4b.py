import csv
with open ('artikel.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter = ';')
    duurste_artikel = 0
    for row in reader:
        prijs = float(reader['Prijs'])
        if prijs > float(row['Prijs']):
            duurste_artikel = prijs
            duurste_naam = row['naam']
        print(duurste_artikel, duurste_naam)
