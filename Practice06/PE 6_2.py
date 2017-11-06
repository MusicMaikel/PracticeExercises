lijst = eval(input('Geef lijst met minimaal 10 strings: '))

output= 0

if lijst < 10.0:
    print('Sorry, de lijst heeft niet het minimale aantal strings.')

for woord in lijst:
    if woord <= 4:
        woord.append(output)

print(output)
