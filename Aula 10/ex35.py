print('Digite o comprimento de 03 reta e descubra se podem formar um triângulo')
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

if a+b>c and a+c>b and b+c>a:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo.')