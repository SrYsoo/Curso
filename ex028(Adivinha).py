from random import randint

print('TENTE ADIVINHAR O NUMERO QUE ESTOU PENSANDO'.center(80))
np = int(input('Digite um numero de 0 a 5 : '))

nc = randint(0,5)

if np == nc: 
    print('Parabens você acertou o numero que eu estava pensando')
else:
    print('Infelizmente você errou KKKKKKKKKKKKKKN\nO numero que eu tinha pensado era {}.'.format(nc))
