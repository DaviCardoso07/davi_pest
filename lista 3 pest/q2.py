#q2
num = int(input("Digite um número positivo: "))
contador = 1

while contador != num:
    contador += 1
    if contador % 2 == 0:
        print(contador)
