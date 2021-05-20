print('-=' * 40)
print('Bem vindo ao Banco Adams, \npara saber sobre disponibilidade de empréstimos preencha as questões a seguir:')
print('-=' * 40)
valor = float(input('Qual o valor o imóvel que deseja comprar? R$'))
salario = float(input('Atualmente, qual o valor do seu salário liquido? R$'))
tempo = int(input('Em quantos anos você pretende dividir as parcelas?'))
parcela = valor / (tempo * 12)
print('-=' * 40)
if parcela <= 0.3 * salario:
    print('Seu sonho pode ser realizado com parcelas de R${:.2f}!!!'.format(parcela))
else:
    print('Infelizmente, no momento não temos um empréstimo com seu perfil, o valor da parcela minima é de {:.2f}, te aguardamos em breve!'. format(parcela))

