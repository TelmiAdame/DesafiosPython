print('=' * 23)
print('Os 10 termos de uma PA')
print('=' * 23)
p = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão:'))
decimotermo = p + (10 - 1) * r #fórmula matemática para descobrir o décimo termo
pa = 1
print('Os 10 termos da PA são:')
while pa != decimotermo:
    pa = pa + r
    print('{} - '.format(pa) if pa != decimotermo else '{}'.format(pa), end=' ')
print('\nFIM')

'''
    RESOLUÇÃO GUANABARA
    
primeiro = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
termo = primeiro
cont = 1
while cont <= 10:
     print('{} - '.format(termo,end=' ')
     termo += razão
     cont += 1
print ('Fim') 

'''