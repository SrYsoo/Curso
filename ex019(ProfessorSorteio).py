from random import choice

a1 = str(input('Prieiro Aluno : '))
a2 = str(input('Segundo Aluno : '))
a3 = str(input('Terceiro Aluno : '))
a4 = str(input('Quarto Alunno : '))
Lista = (a1, a2, a3, a4)

print('O aluno sorteado foi : {}'.format(choice(Lista)))
