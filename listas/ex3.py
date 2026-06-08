def verifica_par(L : list):
    cont_par = 0
    for i in L:
        if i % 2 == 0:
            cont_par += 1
    return f"A lista tem {cont_par} números pares "

lista = []

num = int(input("Digite tantos numeros você quer que seja armazenado na lista: "))

for i in range(num):
    add = int(input(f"Digite o número {i +1}: "))
    lista.append(add)

num_par = verifica_par(L = lista)
print(lista)
print(num_par)

