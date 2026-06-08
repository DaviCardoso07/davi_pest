def calc_media(lista : list):
    soma = 0
    qtd_lista = len(lista)
    for elemento in lista:
        soma += elemento
    media = soma/qtd_lista
    return f"A média da temperatura foi de {media}"

temp = [0, 0, 0, 0, 0, 0, 0]
qtd = len(temp)
for i in range(qtd):
    temp[i] = float(input(f"Digite a temperatura {i+1}: "))

media = calc_media(lista = temp)

def verifica_temp(lista : list, media : float):
    cont = 0
    for elemento in lista:
        if elemento > media:
            cont += 1
    return f"Existem {cont} temperaturas acim da média"

verificacao = verifica_temp(lista = temp, media = media)