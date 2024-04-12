from math import sqrt
c1 = int(input('Digite o Valor do 1 Cateto : '))
c2 = int(input('Digite o Valor do 2 Cateto : '))
mh = sqrt(c1 ** 2 + c2 **2)
print("O comprimento da Hipotenusa é {}. ".format(mh))