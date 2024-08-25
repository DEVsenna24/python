from time import sleep
decisao = str(input('Oi!! gostaria de ver os fogos comigo? \n[SIM]\n[NAO] \n:'))

if decisao == "SIM":
    print('Maneiro!! então fique quetinho que ja vai começar')
    for fogos in range (10, -1, -1):
        print(fogos)
        sleep(2)
    print('bum...bumm...POW')
elif decisao == "NAO":
    dn = str (input('que pena... tem certaza mesmo?\n [TABOM] \n [NAOQUERO]\n:'))
    if dn == 'TABOM':
        print("a que bom, então espra que ja vai começar")
        for fogos in range(10, -1, -1):
            print(fogos)
            sleep(2)
    print('BOOOOMMM...POOOWW')
    if dn == "NAOQUERO":
        print('ta bom, ta bom. Então até a proxima parceiro :( )')
else:
    print('não entendi o que vc falou')