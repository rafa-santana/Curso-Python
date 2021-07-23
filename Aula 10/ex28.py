import random
n = int(input('Advinhe o número que o computador está pensando. *Dica: ele está entre 0 e 5: '))
sorteio = random.randint(0,5)
if n==sorteio: 
    print('Parabéns, eu pensei no número {} e você advinhou!!!'.format (sorteio))
else:
    print('Que pena, não acertou dessa vez... Pensei em {} mas você chutou {}'.format(sorteio,n))
