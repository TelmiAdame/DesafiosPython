# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Escreva um número:'))
sucessor = n - 1
antecessor = n + 1
print('O sucessor de \033[33m{}\033[m é \033[31m{}\033[m e seu antecessor é \033[31m{}\033[m' .format(n, sucessor, antecessor))

