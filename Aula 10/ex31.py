km = float(input('Digite a distância da viagem em Km: '))
if km<=200:
    p = km*0.5
    print('O preço da passagem é R${:.2f}, (R$0,50 por Km)'.format(p))
else:
    p = km*0.45
    print('O preço da passagem é R${:.2f}, (R$0,45 por Km)'.format(p))