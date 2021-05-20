n = int(input('Escreva um númeor inteiro:'))
print('Qual a base de conversão deseja user? \n[1] para binário \n[2] para octal \n[3] para hexadecimal')
base = int(input('Sua opção:'))
binario = bin(n)
octagonal = oct(n)
hexadecimal = hex(n)
if base == 1:
    print('{} convertido para binário é igual {}'.format(n, binario[2:]))
elif base == 2:
    print('{} convertido para octagonal é igual {}'.format(n, octagonal[2:]))
elif base ==3:
    print('{} convertido para hexagonal é igual {}'.format(n, hexadecimal[2:]))
else:
    print('Opção inválida. Tente novamente.')
