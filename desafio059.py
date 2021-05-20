print('Escreva dois valores e escolha uma opção do menu:')
menu = 0
soma = 0
mult = 0
maior = 0
n1 = float(input('\nPrimeiro valor:'))
n2 = float(input('Segundo valor:'))
while menu != 5:
    print('{:^30}\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa'.format('\033[1;34mMENU\033[m'))
    menu = int(input('\nQual número do menu você deseja?'))
    if menu == 1:
        soma = soma + n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif menu == 2:
        mult = mult + n1 * n2
        print('A multiplicação entre {} * {} = {}'.format(n1, n2, mult))
    elif menu == 3:
        maior = n1
        if n1 > n2:
            maior = maior
        else:
            maior = n2
        print('Entre {} e {}, o maior é o valor {}'.format(n1, n2, maior))
    elif menu == 4:
            n1 = float(input('Primeiro valor:'))
            n2 = float(input('Segundo valor:'))
    elif menu == 5:
        print('Programa encerrado!')
    else:
        print('Você digitou um número inválido, tente novamente.')




