import random

a1 = input('Prieiro Aluno : ')
a2 = input('Segundo Aluno : ')
a3 = input('Terceiro Aluno : ')
a4 = input('Quarto Alunno : ')
Lista = (a1, a2, a3, a4)

print('O aluno sorteado foi : {}'.format(random.choice(Lista)))
