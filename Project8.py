status = [
{'situação' : 'Troca de cabo' , 'quantidade' : 30},
{'situação' : 'Necessita de Limpeza' , 'quantidade' : 15},
{'situação' : 'Quebrado ou Inutilizado' , 'quantidade' : 39},
{'situação' : 'Necessita de Limpeza' , 'quantidade' : 74},
{'situação' : 'Quebrado ou Inutilizado' , 'quantidade' : 8},
{'situação' : 'Troca de cabo' , 'quantidade' : 64},
{'situação' : 'Troca de cabo' , 'quantidade' : 20},
      
]
def total_mouses(x):
    total1 = 0
    total1 += x['quantidade']
    return total1


total = map(total_mouses,status)
soma = 0
for c in total:
    soma += c
    
def percentual(x):
    x['percentual'] = (x['quantidade'] / soma) * 100
    return x

status_novo = map(percentual, status)

print('=' * 100)
print(f'Quantidade de mouses: {soma:<40}  ')
print()
a = 'Qtd.'
b = 'Situação'
c = 'Percentual'
print(f'\033[1m{b:<35}{a:<15}{c}\033[m')


for x,c in enumerate(status_novo, start = 1):
    print(f"{x} - {c['situação']:<32}{c['quantidade']:<15}   {round(c['percentual'], 2)} % ")
