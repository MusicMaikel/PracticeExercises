def gemiddelde():
    woorden = input('Voer een zin in: ')
    zinlengte = len(woorden)
    average = str(woorden.split()) / zinlengte
    print(average)

gemiddelde()