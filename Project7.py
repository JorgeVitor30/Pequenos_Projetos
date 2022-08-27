dados = [
{'nome' : 'Jorge' , 'salario' : 1000 },   
{'nome' : 'João' , 'salario' : 5000 },
{'nome' : 'Diego' , 'salario' : 600 },    
{'nome' : 'Luana' , 'salario' : 1500 },    
{'nome' : 'Pedro' , 'salario' : 400 },    
{'nome' : 'Levy' , 'salario' : 1000 },    
{'nome' : 'Barros' , 'salario' : 250 },    

]


def adicional(p):
    if p['salario'] * 0.2 < 100:
        p['extra'] = 100
    else:
        p['extra'] = p ['salario'] * 0.2  
        
    return p 
    

mapeado = map(adicional,dados)    # USEI O MAP PRA DEFINIR A NOVA VARIÁVEL DO DINHEIRO EXTRA

a = list(mapeado)

sal = map(lambda x: x['salario'],a)
extra = map(lambda i: i['extra'],a) 
  

print()
print()
print('\033[1;30mProjeção de Gastos com Abono')
print('='*30)
print('\033[1;32mSALÁRIO                  EXTRA \033[m')
print()



    
total = min = 0
maior = []
for y in sal:
    d = y * 0.2
    if d < 100:
        d = float(100)
        min += 1
    total += d
    maior.append(y * 0.2)
    
    
    print(f'\033[1;21mSalário: R$: {y:<10}  R$ {d}\033[m')
    
print()
print(f'\033[1;32mForam um total de {len(a)} Colaboradores ')
print(f'Total gasto com abonos: R$ {total}')
print(f'Valor mínimo pago a {min} colaboradores')
print(f'Maior valor de abono pago: R$ {max(maior)}\033[3m')
print()

    
