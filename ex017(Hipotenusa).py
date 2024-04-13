from math import sqrt
c1 = float(input('Digite o Valor do 1 Cateto : '))
c2 = float(input('Digite o Valor do 2 Cateto : '))
mh = sqrt(c1 ** 2 + c2 ** 2)
print("O comprimento da Hipotenusa é {:.2f}. ".format(mh))
