import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hipot = math.hypot(co,ca)
print ('O valor da hipotenusa é: {}'.format(hipot))