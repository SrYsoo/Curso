print('Você esta digirindo um SKYLINE GT-R '.center(80))

vc = int(input('Em qual velocidade você esta andando ? '))

mu = (vc - 80) * 7

if vc > 80:
    print('Você foi multando em R${} ao ultrapassar o limite de velocidade de 80 Km/h.'.format(mu))
else:
    print('Parabens você ficou dentro do limite de velocidade')
