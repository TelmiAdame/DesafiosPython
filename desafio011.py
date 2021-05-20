h = float(input('Qual a altura da parede?'))
l = float(input('Qual a largura da parede?'))
area = h * l
tinta = area / 2
print('Para pintar está parede de {}m² você vai precisar de {:.2f} litros de tinta.'.format(area, tinta))
