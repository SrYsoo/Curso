fr = str(input('Digite uma frase : ')).lower()

print('A letra A aparece {} vezes.'.format(fr.count('a')))
print('A letra A aparece na posição {} '.format(fr.find('a')+1))
print('A ultima posição da letra A aparece é {} '.format((fr.rfind('a')+1)))
