n = int(input('Digite o número e descubra seu fatorial:'))
contagem = n
fatorial = 1
print('Calculando {}! ='.format(n), end=' ')
while contagem > 0:
    print('{}'.format(contagem), end=' ')
    print('x' if contagem > 1 else '=', end=' ')
    fatorial = fatorial * contagem
    contagem = contagem - 1
print('{}'.format(fatorial))
# Resolução do Guanabara, a minha está em baixo, eu tive muitos pontos em comum, mas erroneamente achei que precida usar o for e o while, por isso me confundi muito.

'''n = int(input('Digite um número para calcular o fatorial:'))
multiplicando = n
multiplicandor = 1
resultado = 0
print('Calculando {}! ='.format(n), end=' ')
for c in range(1, n + 1):
    multiplicando = c
    multiplicandor = c - 1
    while c < 1:
        resultado = multiplicando * multiplicandor
    if c != 1:
        print('{} X'.format(multiplicando), end=' ')
    else:
        print('{}'.format(multiplicando), end=' ')
print('= {}'.format(resultado))'''
