cadastro = []
dados = []

def interface():
    print('''
1 - inserir uma nova veículo
2 - Mostrar quantos carros cadastrados
3 - mostrar/imprimir dados de uma veículo com base no código
4 - mostrar/imprimir todas as veículos de um servidor
5 - mostrar/imprimir todas as veículos de um servidor em ordem alfabética pelo nome 
6 - sair do programa
          ''')
  
while True:   
    interface()
    escolha = int(input('Digite um valor pra escolha: '))
    if escolha == 6:
        break
    
    if escolha == 1:
        dados.append(int(input('Código do veiculo: ')))
        dados.append(str(input('Desc. do veiculo: ')))
        dados.append(input('Marca do veiculo: '))
        dados.append(input('Placa veiculo: '))
        dados.append(input('Modelo do veiculo: '))
        dados.append(str(input('Digite seu nome: ')))
        print()
        print('\033[1;33m Cadastrado com Sucesso \033[m')
        cadastro.append(dados[:])
        dados.clear()
        

    
    if escolha == 4:
        for x in range(0,len(cadastro)):
            print('-=' * 13)
            for c in cadastro[x]:
                print(c)
            print('-=' * 13)    
                
    if escolha == 3:
        sort = sorted(cadastro, key = lambda i: i[0])
        print('-=' * 13)
        for x in range(0,len(sort)):
            for c in sort[x]:
                print(c)
            print('-=' * 13)
         

        
        
    if escolha == 5:
        print('-=' * 13)
        sort1 = sorted(cadastro, key = lambda x: x[5])
        for x in range(0,len(sort1)):
            for c in sort1[x]:
                print(c)
            print('-=' * 13)
    print()
    if escolha == 2:
        print(f'\033[1;33mExistem {len(cadastro)} carros cadastrados no estacionamento\033[m')
        

                    
            
