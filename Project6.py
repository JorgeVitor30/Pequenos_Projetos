print('Digite abaixo DOIS números para o intervalo!')
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
soma = 0
if x < y:
    for itv1 in range(x, y+1, 1):
        print(f'{itv1}', end='  ')
        if itv1 % 13 != 0:
            soma += itv1

    print(
        f'---> \033[1;32m{soma}\033[m \033[1;33m( A SOMA DE TODOS OS NÃO MÚLTIPLOS DE 13) \033[m')

if x > y:
    for itv1 in range(x, y - 1, -1):
        print(f'{itv1}', end='  ')
        if itv1 % 13 != 0:
            soma += itv1

    print(
        f'---> \033[1;32m{soma}\033[m \033[1;33m( A SOMA DE TODOS OS NÃO MÚLTIPLOS DE 13) \033[m')

if x == y:
    if x % 13 != 0:
        print(f'--> {x} ( A SOMA DE TODOS OS NÃO MÚLTIPLOS DE 13)')
    else:
        print(
            f'--> \033[1;32m{0}\033[m \033[1;33m(A SOMA DE TODOS OS NÃO MÚLTIPLOS DE 13)\033[m')
