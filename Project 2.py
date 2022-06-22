def linha(tam=42):
    print('-' * tam)


lista = list()
while True:
    a = int(input('Digite um valor: '))
    lista.append(a)
    if a == -1:
        lista.pop()
        break
linha()
print(f'Foram Lidos {len(lista)} valores')
linha()
print(f'Os números: {lista}', end=' ')
print()
linha()
print(f'Os números inversos: {sorted(lista,reverse = True)}')
linha()
print(f'A soma dos números é: {sum(lista)}')
linha()
print(f'A média dos números é {sum(lista) / len(lista) :.2f}')
linha()
print('Os números acima da média é: ', end='')
for x in lista:
    if x > (sum(lista) / len(lista)):
        print(f'{x},', end=' ')
print()
linha()
print('Os valores Abaixo de 7: ', end = '')
for x in lista:
    if x < 7:
        print(x, end = ' ')
        
print()
print('\033[1;32mOBRIGADO POR TESTAR ESSE PROGRAMA!!! VOLTE SEMPRE\033[m')
