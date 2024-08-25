soma = 0
cont = 0
for multiplos in range(1,501,2):
    if multiplos % 3 == 0 :
       soma = soma + multiplos
       cont = cont + 1
print('as somas dos {} valores vai da {}'.format(cont,soma))
    
