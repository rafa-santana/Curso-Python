import random
a1 = input ('Digite o nome do 1º aluno: ')
a2 = input ('Digite o nome do 2º aluno: ')
a3 = input ('Digite o nome do 3º aluno: ')
a4 = input ('Digite o nome do 4º aluno: ')
sorteio = random.choice ([a1,a2,a3,a4])
print  ('O aluno sorteado para apagar o quadro foi: {}'.format(sorteio))