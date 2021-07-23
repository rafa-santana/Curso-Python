ano = int(input('Digite um ano: '))

if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print('{} é um ano Bissexto'.format(ano))
        else:
            print('{} não é um ano Bissexto'.format(ano))
    else:
        print('{} é um ano Bissexto'.format(ano))
else: 
    print('{} não é um ano Bissexto'.format(ano))