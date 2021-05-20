pesomaior = 0
pesomenor = 0
for c in range(0, 5):
    peso = float(input('Qual seu peso?'))
    if pesomenor == 0 and pesomaior == 0:
        pesomenor = peso
        pesomaior = peso
    elif peso > pesomaior:
        pesomaior = peso
    elif peso < peso:
        pesomaior = pesomaior
    elif peso > pesomenor:
        pesomenor = pesomenor
    elif peso < pesomaior:
        pesomenor = peso
print('O menor peso é {} e o maior peso é {}.'.format(pesomenor, pesomaior))


