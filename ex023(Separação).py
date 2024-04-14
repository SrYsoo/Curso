n = str(input('Digite um número : '))

print('Unidade : {}'.format(n[3]))
print('Dezena : {}'.format(n[2]))
print('Centena : {}'.format(n[1]))
print("Milhar: {}".format(n[0]))

#nao funciona com numero de 3 digitos

#------------------------------------------------------------------------------------------

#usando a matemática

n2 = int(input('Digite um valor : '))

u = n2 // 1 % 10
d = n2 // 10 % 10
c = n2 // 100 % 10
m = n2 // 1000 % 10

print('Unidade: {} '.format(u))
print('Dezena:  {} '.format(d))
print('Centeza: {} '.format(c))
print('Milhar:  {}'.format(m))
