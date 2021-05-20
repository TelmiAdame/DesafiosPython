print('-*' * 20)
print(' =========== LOJAS TELMI ============== \nDescubra de quanto é o seu desconto:')
print('-*' * 20)
valor = float(input('Qual o valor da sua compra? R$'))
formadepagamento = str(input('Qual da forma de pagamento?'))
if formadepagamento == ' à vista':
    print('À vista em dinheiro ou cheque seu produto saíra: R${:.2f}.'.format(valor - valor * 0.10))
elif formadepagamento == ' parcelado':
    numerodeparcelas = int(input('Em quantas vezes deseja parcelar ?'))
    if numerodeparcelas == 1:
        print('À vista no cartão o seu produto sairá por R${:.2f}.'.format(valor - valor * 0.05))
    if numerodeparcelas == 2:
        print('Caso prefera pagar em 2x no cartão o valor do produto será o mesmo R${:.2f}.'.format(valor))
    else:
        print('Caso prefira pagar em 3x ou mais no cartão o valor de cada parcela será de {:.2f}.'.format(valor + (valor * 0.20 * numerodeparcelas / numerodeparcelas)))
#eu anotei a resolução do Guanabara no caderno tb




