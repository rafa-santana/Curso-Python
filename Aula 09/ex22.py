frase = input('Digite o seu nome completo: ')
print ('Nome em maiúsculo: {}'. format(frase.upper()))
print ('Nome em minúsculo: {}'.format(frase.lower()))
let = len(frase)
esp = frase.count(' ')
total = int(let-esp)
print ('Quantidade total de letras: {}'.format(total))
dividido = frase.split()
let1nome = len(dividido[0])
print ('Quantidade de letras no primeiro nome: {}'.format(let1nome))
