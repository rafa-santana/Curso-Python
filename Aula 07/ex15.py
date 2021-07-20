km = float(input('Digite a quantidade de km percorridos: '))
d = float(input('Digite a quantidade de dias que o veículo foi alugado: '))
p = (km*0.15)+(d*60)
print('O preço a pagar pelo carro alugado é: R${:.2f}'.format(p))