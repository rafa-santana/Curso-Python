s = float(input ('Digite o seu salário: '))
if s>1250:
    print('O seu salário de R${} sofrerá um aumento de 10 porcento, e será: R${:.2f} '.format(s,s+(s*0.1)))
else:
    print('O seu salário de R${} sofrerá um aumento de 15 porcento, e será: R${:.2f} '.format(s,s+(s*0.15)))