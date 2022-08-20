lista_de_inteiros = [ 
[1,2,3,4,5,6,7,8,9,10],
[3,4,5,5,6,7,8,9,1,2],
[5,6,4,3,2,7,8,9,6,1],                
[4,5,6,7,8,9,7,5,4,3],                    
[4,3,2,2,1,5,6,7,8,9],                     
[5,6,7,8,9,0,7,5,0,4],                    
[3,4,3,2,2,1,5,6,7,8],                    
[4,5,6,7,8,9,9,8,7,5],
[10,5,6,7,8,9,4,3,2,1],                     
                                        
                     ]


def encontra_primeiro_duplicado(lista_de_numeros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    for numero in lista_de_numeros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
    
        numeros_checados.add(numero)
    return primeiro_duplicado

for x in lista_de_inteiros:
    print(encontra_primeiro_duplicado(x), x)
