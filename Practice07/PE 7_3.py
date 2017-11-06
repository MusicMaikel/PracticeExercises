cursus = {'Jan':7.1, 'Piet':4.0}

for naam in cursus:
    if cursus[naam] > 9.0:
        print(naam, cursus[naam])
    else:
        print('Niemand heeft een 9 gehaald')
