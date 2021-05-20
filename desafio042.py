print('Descubra se é possivel construir um triângulo com seus segmentos:')
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro Segmento:'))
if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
    print('Com esses segmentos é possível construir um triângulo!', end='')
    if s1 == s2 == s3:
        print(' O triângulo será equilátero!')
    elif s1 == s2 or s1 == s3 or s2 == s3:   # ou else:
        print('O triângulo será isósceles!')
    elif s1 != s2 and s1 != s3 and s2 != s3 and s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:  # ou s1 =! s2 =! s3 != s1:
        print('O triângulo será escaleno!')
else:
    print('Com esses segmentos não é possível construir um triângulo!')


