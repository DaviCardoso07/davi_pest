
def verifica_prod(prod : list, limite : int = 10):
    cont = 0
    for i in prod:
        if i < limite:
            cont += 1
    return f"Temos {cont} produtos no estoque menor que {limite}"

prod = [0, 0, 0, 0, 0]

qtd = len(prod)
for i in range(qtd):
    prod[i] = float(input(f"Digite o produto {i+1}: "))

print(verifica_prod(prod = prod))



        