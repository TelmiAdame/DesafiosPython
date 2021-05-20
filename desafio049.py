n = int(input('Qual número deseja saber a tabuada?'))
for c in range(0, 11):
    print('{} * {} = {}'.format(n, c, (n * c)))
