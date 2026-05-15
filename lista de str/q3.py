#q3
def troca_palavra(str):
    palavra = str[1:]
    palavra_nova = "0" + palavra
    print(f"A palavra nova -> {palavra_nova}")

palavra = input("Digite uma palavra: ")

troca_palavra(str = palavra)