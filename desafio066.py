soma = total = 0
while True:
    n = int(input('Digite um número [para parar digite 999]:'))
    if n == 999:
        break
    soma = soma + n
    total = total + 1
print(f'Foram digitados {total} e a soma deles é igual a {soma}.')
