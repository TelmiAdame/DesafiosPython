print('=' * 20)
print('\033[1;33;40m10 TERMOS DE UMA PA\033[m')
print('=' * 20)
n = int(input('Qual o primeiro termo?'))
r = int(input('Qual a razão?'))
f = n + (10 - 1) * r #fórmula matemática para descobrir o décimo termo
for n in range(n, f, r):
    print(n, end=' * ')
