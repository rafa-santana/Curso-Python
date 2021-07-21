import math
ang = float (input('Digite o valor de um ângulo e descubra o seu seno, cosseno e tangente: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print ("Seno = {}, cosseno = {} e tangente = {}".format(sen, cos, tan))