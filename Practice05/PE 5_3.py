infile = open('kaartnummer.txt', 'r').readlines()
count = 0
enter = '\n'
for enter in infile:
    res = count + 1
    print(res)
