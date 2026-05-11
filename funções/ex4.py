def verifica_se_dentro(x, y):
    if x >= 2 and x <= 6 and y >= 3 and y <= 5:
        return f"P( {x},{y})  está dentro"
    else:
        return f"P({x},{y}) está fora"
        
print(verifica_se_dentro(4, 4))
print(verifica_se_dentro(5, 4))
print(verifica_se_dentro(6, 3))
print(verifica_se_dentro(5.5, 5.5))

#OBS: Para printar o return, é necessário ou usar o print como eu fiz acima,
#ou colocar a função dentro de uma variável e dps printar a variável

#Exemplo:

verificacao = verifica_se_dentro(4, 4)
print(verificacao)

