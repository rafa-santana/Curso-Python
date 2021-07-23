print('Digite 03 números e descubra qual o maior e qual o menor')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1>n2 and n1>n3:
    print('O maior número é: {}'.format(n1))
    if n2>n3:
        print('O menor número é: {}'.format(n3))
    else:
        print('O menor número é: {}'.format(n2))

if n2>n1 and n2>n3:
    print('O maior número é: {}'.format(n2))
    if n1>n3:
        print('O menor número é: {}'.format(n3))
    else:
        print('O menor número é: {}'.format(n1))

if n3>n2 and n3>n1:
    print('O maior número é: {}'.format(n3))
    if n2>n1:
        print('O menor número é: {}'.format(n1))
    else:
        print('O menor número é: {}'.format(n2))
