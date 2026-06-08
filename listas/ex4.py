lista = [67, 67, 6, 2]

def verifica_lista(L : list):
    L_par = []
    for i in range(len(L)):
        if L[i] % 2 == 0:
            L_par.append(L[i])
    return f"Nova lista -> {L_par}"

nova_L = verifica_lista(L = lista)

print(nova_L)