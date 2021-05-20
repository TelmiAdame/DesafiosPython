n = int(input('Qual número?'))
contar = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        contar = contar + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[m\nO número {} foi divisivel {} vezes.'.format(n, contar))
if contar == 2:
    print('Logo, {} é um número prim0'.format(n))
else:
    print('Logo o número {} NÃO é um número primo.'.format(n))







