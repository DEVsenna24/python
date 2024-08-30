soma = 0
cont = 0
for c in range(1, 7):
    num1= int(input('numero {}:\n'.format(c)))
    if num1 % 2 == 0:
        soma += num1
        cont += 1
    elif num1 % 2 != 0:
       num1= int(input('numero {}:\n'.format(c)))
       soma += num1
       cont += 1 
print('vc informou {} numero , dando o a soma total de {} numeros'.format(cont, soma))
