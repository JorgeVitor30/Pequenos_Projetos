for x in range(1, 6):
    nome = str(input('Digite o nome: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    nasc = int(input('Digite o ano de nascimento: '))
    idade = 2022 - nasc
    status = str(input('Digite o seu status: [comum,especial]: ')).upper()
    contri = int(input('Quantos anos de contribuição?: '))
    print('-=' * 25)
    print(f'Pessoa {x}: {nome} de {idade} anos .')
    if status == 'COMUM':
        if sexo == 'M':
            if idade >= 65 and contri >= 35:
                print('Situação: APTO')
            else:
                print('Situação: NÃO APTO')
    if status == 'COMUM':
        if sexo == 'F':
            if idade >= 60 and contri >= 30:
                print('Situação: APTO')
            else:
                print('Situação: NÃO APTO')
    if status == 'ESPECIAL':
        if sexo == 'M':
            if idade >= 60 and contri >= 30:
                print('Situação: APTO')
            else:
                print('Situação: NÃO APTO')
    if status == 'ESPECIAL':
        if sexo == 'F':
            if idade >= 55 and contri >= 25:
                print('Situação: APTO')
            else:
                print('Situação: NÃO APTO')
    print('-=' * 25)
