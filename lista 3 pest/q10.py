inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))


while inicio <= fim:
    soma = 0
    div = 1
    
    while div < inicio:
        if inicio % div == 0:
            soma = soma + div
        div +=1
    if soma == inicio:
        print(f"{inicio} é um número perfeito")
     
    inicio+=1
    