def calc_media (L : list, contador : int):
    MP = cont/len(L)
    if MP >= 6:
        return f"Parabéns, você está aprovado, sua média foi {MP}"
    elif MP <3:
        return f"você foi reprovado, sua média foi {MP}"
    else:
        print("Você ficou de prova final")
        PF = float(input("Digite sua nota da prova final: "))
        MF = (MP+PF)/2
        if MF >=5:
           return f"Parabéns, você está aprovado, sua média final foi {MF}"
        else:
            return f"você foi reprovado, sua média final foi {MF}"

def ler_lista():
    lista = [0, 0, 0, 0, 0]
    for i in range(5):
        lista[i] = float(input(f"Digite a {i+1}º nota: "))
    return lista

def contador(L : list):
    cont = 0
    for item in L:
        cont += item
    return cont

lista = ler_lista()
cont = contador(L = lista)

print(calc_media(L = lista, contador = cont))