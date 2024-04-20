a = int(input('Primeiro : '))
b = int(input('Segundo : '))
c = int(input('Terceiro : '))

li = a, b, c

sorted(li)

if li[0] + li[1] > li[2]:
    print('Sim, pode ser um triangulo.')
else:
    print('Não, pode ser um triangulo.')
