#q2
def ler_str(str : str):
    tam = len(str)
    for i in range(1, tam):
        print(str[-i])
    print(str[0])

palavra = input("Digite uma palavra: ")

ler_str(str = palavra)
