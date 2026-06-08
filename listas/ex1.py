def calcula_media(L : list):
    cont = 0
    for item in L:
        cont += item
    return cont/len(L)

qtd_notas = 5
notas = [0, 0, 0, 0, 0]

for i in qtd_notas:
    notas[i] = float(input(f"Digite a nota"))
print(notas)

media = calcula_media(notas)
print(f"A média foi de {media}")
