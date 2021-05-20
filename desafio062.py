primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razão:'))
termo = primeiro
contagem = 1
pergunta1 = 'SIM'
pergunta2 = 1
while contagem <= 10:
    contagem = contagem + 1
    termo = termo + razao
    print(termo, end=' ')
pergunta1 = str(input('\nDeseja mostrar mais alguns termos?').upper())
while pergunta1 == 'SIM' and pergunta2 != 0:
    pergunta2 = int(input('\nQuantos termos a mais gostaria de ver?'))
    if pergunta2 != 0:
        pergunta2 = pergunta2 + 10
        termo = primeiro
        contagem = 1
        while contagem <= pergunta2:
            contagem = contagem + 1
            termo = termo + razao
            print(termo, end=' ')
    else:
        print('END')



