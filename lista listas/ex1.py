#ex1

def calc_lista():
    lista = [0,0,0,0,0]
    for i in range(5):
        lista[i] += float(input(f"Digite a nota {i+1}: "))
    return lista

lista = calc_lista()

def calc_media(notas : list):
    cont = 0
    for i in notas:
        cont += i
    media = cont/len(notas)
    return media

media = calc_media(notas = lista)

def verifica_nota(media : float):
    if media >= 6:
        print(f"Parabéns, você foi aprovado com média {media}")
    else:
        print(f"Você foi reprovado com média {media}")

verifica_nota(media = media)