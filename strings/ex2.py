def verificar_str(string : str):
    tam = len(string) #função que  ler o número de caracteres de uma str, int, float e etc
    for i in range(tam):
        if (string[i] == "a") or (string[i] == "A"):
            return True
    
    return False

minha_string = "Aberto"

if verificar_str(minha_string) == True:
    print(f"Tem letra 'A' na string {minha_string}")
else:
    print(f"Não tem letra 'A' na {minha_string}")
