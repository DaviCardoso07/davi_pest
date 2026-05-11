def pegar_intervalo (str : str, int1 : int, int2 : int ):
    intervalo = str[int1:int2]
    return intervalo

print(pegar_intervalo("Abacaxi", 1, 5))