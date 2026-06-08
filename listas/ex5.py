def remove_numero(L : list, N : int):
    if N in L:
        L.remove(N)
    else:
        print(f"Número não existe")
    return L

lista = []
verif_l = 0
while True:
    verif_l = int(input("Digite um número(caso queira parar digite -1): "))
    if verif_l == -1:
        break
    else:
        lista.append(verif_l)
    
N_rem = int(input("Digite um número para remover: "))

nova_L = remove_numero(L = lista, N = N_rem)

print(nova_L)