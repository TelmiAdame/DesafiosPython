import math
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do adjacente?'))
h = math.hypot(co,ca)
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(h))

from math import hypot
co = float(input('Qual o comprimento do cateto oposto?'))
ca = float(input('Qual o comprimento do adjacente?'))
print('A hipotenusa desse triângulo retângulo é {:.2f}'.format(hypot(co, ca)))
