def temperatuur(TempCelsius):
    TempFahrenheit = TempCelsius * 1.8 + 32
    return TempFahrenheit

def table():
    for TempCelsius in range (-30, 40, 10):
        print(('{:5}' '{:4}'.format(temperatuur(TempCelsius), TempCelsius)))

print(table())
