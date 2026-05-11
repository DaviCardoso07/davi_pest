def verificar_vogal(string : str):
    tam = len(string)
    for i in range(tam):
        if (string[i] == "A") or (string[i] == "a") or (string[i] == "E") or (string[i] == "e") or (string[i] == "I") or (string[i] == "i") or (string[i] == "O") or (string[i] == "o") or (string[i] == "U") or (string[i] == "u"):
            return True
    return False

string_do_usuario = input("Digite sua str: ")

if verificar_vogal(string_do_usuario) == True:
    print("Tem vogal")
else:
    print("Não tem vogal")
