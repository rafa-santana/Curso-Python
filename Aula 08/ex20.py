import random
a1 = input ('Digite o nome do 1º aluno: ')
a2 = input ('Digite o nome do 2º aluno: ')
a3 = input ('Digite o nome do 3º aluno: ')
a4 = input ('Digite o nome do 4º aluno: ')
sorteio = random.sample ([a1,a2,a3,a4], k=4)
print('A ordem de apresentação sorteada foi: {}'.format(sorteio))