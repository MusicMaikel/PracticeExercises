import xmltodict

def processXML(filename):
    import xmltodict
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

stationsdict = processXML('FA.xml')
stations = stationsdict['Stations']['Station']

print('Dit zijn de codes en types van de 4 stations: ')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print('Dit zijn alle stations met één of meer synoniemen: ')
for station in stations:
    if station['Synoniemen'] is not None:
        print('{:4} - {}'.format(station['Code'], station['Synoniemen']))

print('Dit is de lange naam van elk station: ')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))

