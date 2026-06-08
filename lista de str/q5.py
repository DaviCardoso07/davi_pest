#q5

def verifica_vogal(palavra : str):
    tam = len(palavra)
    total = 0
    for i in range(tam):
        letra = palavra[i]
        if letra == "a" or letra == "A" or letra == "e" or letra == "E" or letra == "i" or letra == "I" or letra == "o" or letra == "O" or letra == "u" or letra == "U":
            total += 1
    print(f"A palavra digitada -> {palavra} tem um total de {total} vogais")

string = input("Digite uma palavra: ")

verifica_vogal(palavra = string)