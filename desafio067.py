print('=-' * 20)
print(' ' * 10, 'TABUADA')
print('=-' * 20)
while True:
    n = int(input('\nDe qual número deseja ver a tabuaba completa?'))
    if n < 0:
        break
    else:
        c = 0
        r = 0
        while c < 10:
            c = c + 1
            r = n * c
            print(f'{n} x {c} = {r}')
print('PROGRAMA ENCERRADO, OBRIGADA!')