carros = [
    ['gol', 10],
    ['fusca', 7],
    ['uno', 12.5],
    ['vectra', 9],
    ['peugeout', 14.5]

]
cont = 0
eco = list()
for x in carros:
    eco.append(carros[cont][1])
    cont += 1
a = max(eco)
print(f'O carro mais econômico é o {carros[eco.index(a)][0]} com {a} Km/L')

cont = 0
consumo = list()
for x in carros:
    consumo.append(carros[cont][1])
    cont += 1


