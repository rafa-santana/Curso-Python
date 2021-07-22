frase = input ('Digite uma frase: ')
frase = frase.lower()
print ('A frase possui {} letras "a"'.format(frase.count('a')))
print ('A posição que ela aparece a primeira vez é: {}'.format(frase.find('a')))
print ('A posição que ela aparece a última vez é: {}'.format(frase.rfind('a')))

