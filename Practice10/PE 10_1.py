def processXML(filename):
    import xmltodict
    with open(filename) as myXMLFile:
        filecontentstring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filecontentstring)
        return xmldictionary

voorbeeldendict = processXML('artikelen.xml')
voorbeelden = voorbeeldendict['artikelen']['artikel']

for voorbeeld in voorbeelden:
    if voorbeeld ['naam'] is not None:
        print(voorbeeld['naam'])