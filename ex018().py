from math import cos, tan, sin, radians

An = float(input('Qual é o ângulo?'))

se = sin(radians(An))
tan = tan(radians(An))
cos = cos(radians(An))

print('Seno: {:.2f}'.format(se))
print('Cosseno: {:.2f} '.format(cos))
print('Tangente: {:.2f} '.format(tan))
