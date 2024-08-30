print('===PROGREÇÃO ARITMÉDICA==== ')

pt= int(input('informe o primeiro termo:'))
rz= int(input('informe a razão:'))
soma= pt + (10 - 1) * rz
for c in range(pt,soma + rz, rz):
    print('{}'.format(c), end ='- ')
print('acabou')