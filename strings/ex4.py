def verificar_maior(str1 : str, str2 : str):
    c1 = len(str1)
    c2 = len(str2)
    if c1 > c2:
        print("A string 1 é maior")
    elif c1 < c2:
        print("A string 2 é maior")
    else:
        print("Tem os mesmos tamanhos")
    
meu_str1 = input("Digite str1: ")
meu_str2 = input("Digite str2: ")

verificar_maior(str1 = meu_str1, str2 = meu_str2)