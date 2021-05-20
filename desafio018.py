import math
a = int(input('Escreve um ângulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O angulo {} possui seno {:.2f}, cosseno {:.2f} e a tangente {:.2f}'.format(a, s, c, t))

from math import radians, cos, sin, tan
a = int(input('Escreve um ângulo:'))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O angulo {} possui seno {:.2f}, cosseno {:.2f} e a tangente {:.2f}'.format(a, s, c, t))

