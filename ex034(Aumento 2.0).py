from time import sleep

print('VOCÊ RECEBERA UM AUMENTO DE SALARIO .'.center(80))
sa = float(input('Quanto é o seu salario ?'))

print('CALCULANDO'.center(80))
sleep(2)

if sa >= 1250:
    novo = sa + (sa * 10  / 100)
    print('1Seu salario aumentou para {}R$'.format(novo))
else:
    novo = sa + (sa * 15 / 100)
    print('2Seu salario aumentou para {}R$'.format(novo))
