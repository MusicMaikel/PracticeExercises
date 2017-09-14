paspoort = input('Bent u in het bezit van een Nederlands paspoort? (ja/nee): ')
leeftijd = eval(input('Wat is uw leeftijd?: '))

if leeftijd >= 18 and paspoort == 'ja':
    print('Gefeliciteerd, je mag stemmen!')
