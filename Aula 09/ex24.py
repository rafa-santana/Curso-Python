cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.upper()
dividido = cidade.split()
r = 'SANTO' in dividido[0]
print("O nome da cidade começa com SANTO? {} ".format(r))