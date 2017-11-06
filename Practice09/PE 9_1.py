try:
    bedrag = 4356
    aantal = eval(input('Geef het aantal reizigers: '))
    if aantal < 0:
        print('Reizen met 0 personen is niet mogelijk.')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    print('Delen door 0 mag niet.')
except NameError:
    print('Geef cijfers weer in de vorm van cijfers, geen letters.')
except:
    print('Onjuiste invoer')
