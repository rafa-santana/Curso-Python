v = float(input('Digite a velocidade do seu carro: '))
if v>80:
    multa = (v-80)*7
    print ('Você ultrapassou o limite de 80Km/h desta via, valor da multa: R${:.2f}'.format(multa))
