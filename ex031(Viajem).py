print('VIAJAR'.center(80))

km = float(input('A sua viajem sera de quantos Km ?'))

if km >= 200:
    print('A sua viajem saira por R${},cobrando R$0,45 por Km'.format(km*0.45))
else:
    print('A sua viajem saira por R${},cobrando R$0,50 por Km'.format(km*0.50))

