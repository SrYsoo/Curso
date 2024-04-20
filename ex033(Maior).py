from time import sleep

a = int(input('Primeiro Valor : '))
b = int(input('Segundo Valor : '))
c = int(input('Terceiro Valor : '))

print('Calculando...'.center(80))
sleep(3)

menor = a
if b < a  and  b < c :
    menor = b
if c < a and c < b :
    menor = c

maior = a 
if b > a and b > c : 
    maior = b
if c > a and c > b :
    maior = c

print('Menor : {}'.format(menor))
print('Maior : {}'. format(maior))
