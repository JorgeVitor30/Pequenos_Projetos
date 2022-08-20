def menu():
    print('''
1- Adição
2- Substração
3- Multiplicação
4- Divisão 
5- Exit
          ''')

    
while True:
    print('-=' * 25)
    menu()
    print('-=' * 25)
    escolha = int(input('Escolha:'))
    if escolha == 5:
        break
    if escolha == 1:
        n1 = int(input('1:'))
        n2 = int(input('2:'))
        print(f'{n1} + {n2} = {n1 + n2}')
    if escolha == 2:
        n1 = int(input('1:'))
        n2 = int(input('2:'))
        print(f'{n1} - {n2} = {n1 - n2}')
    if escolha == 3:
        n1 = int(input('1:'))
        n2 = int(input('2:'))
        print(f'{n1} * {n2} = {n1 * n2:.2f}')
    if escolha == 4:
        n1 = int(input('1:'))
        n2 = int(input('2:'))
        print(f'{n1} / {n2} = {n1 / n2:.2f}') 
    else:
        print('Opção Inválida') 
