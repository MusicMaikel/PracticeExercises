infile = open('Kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()

for regel in regels:
    kaartinfo = regel.split(',')
    print(kaartinfo[1].strip() + ' heeft kaarnummer: ' + kaartinfo[0].strip())
