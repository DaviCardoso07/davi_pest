#ex3
def acha_maior(lista : list):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

lista = [0, 0, 0, 0, 0]
qtd = len(lista)

for i in range(qtd):
    lista[i] = int(input(f"Digite a nota {i+1}: "))

print(f"O maior número é {acha_maior(lista = lista)}")

