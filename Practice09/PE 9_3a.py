import csv
with open ('homos.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter = ';')
    hoogste_score = 0
    for row in reader:
        score = int(row[2])
        if score > hoogste_score:
            hoogste_score = score
            hoogste_naam = row[0]
            hoogste_datum = row[1]
        print(hoogste_score, hoogste_naam, hoogste_datum)

