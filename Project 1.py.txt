def menu(txt):
    print('-=' * 15)
    print(txt.center(30))
    print('-=' * 15)


def cabecalho(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1


contagens = []
cont_ws = 0
cont_ux = 0
cont_lx = 0
cont_nw = 0
cont_mos = 0
cont_ot = 0

votos = list()
while True:
    menu('Qual o melhor Sistema Operacional para uso em servidores? ')
    cabecalho(['Windows Server', 'Unix', 'Linux',
              'Netware', 'Mac OS', 'Outro'])
    print('7 para sair')
    enquete = int(input('As Possiveis Respostas: '))
    if enquete == 0:
        print()
        print()
        print('\033[1;31mEncerrando... \033[m')
        break

    if enquete == 1:
        cont_ws += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')
    if enquete == 2:
        cont_ux += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')
    if enquete == 3:
        cont_lx += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')
    if enquete == 4:
        cont_nw += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')
    if enquete == 5:
        cont_mos += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')

    if enquete == 6:
        cont_ot += 1
        print('\033[1;32m Seu voto foi COMPUTADO! \033[m')

    if enquete == 7:
        break
total = cont_ws + cont_ux + cont_lx + cont_mos + cont_ot + cont_nw
a = 'Windows Server'
b = 'Unix'
c = 'Linux'
d = 'Netware'
e = 'Mac OS'
f = 'Outro'
abc = 'Sistema Operacional'
dcf = 'Votos'
pr = '%'
r = 'Total'
print()

print(f'{abc:>10} {dcf:>20} {pr:>15}')
print('-' * 60)
print(f' {a:<10} {cont_ws:>21} {(cont_ws/total) * 100 :>20.2f} %')
print(f' {b:<10} {cont_ux:>25} {(cont_ux/total) * 100 :>20.2f} %')
print(f' {c:<10} {cont_lx:>25} {(cont_lx/total) * 100 :>20.2f} %')
print(f' {d:<10} {cont_nw:>25} {(cont_nw/total) * 100 :>20.2f} %')
print(f' {e:<10} {cont_mos:>25} {(cont_mos/total) * 100 :>20.2f} %')
print(f' {f:<10} {cont_ot:>25} {(cont_ot/total) * 100 :>20.2f} %')
print('-' * 60)
print(f'\033[33m{r:>5}\033[m \033[32m{total: > 31}\033[m')
