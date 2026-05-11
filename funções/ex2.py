base = int(input("Digite a base: "))
altura = int(input("Digite a altura: "))

def calcular_area(base, altura):
    area = base * altura
    print(f"base = {base}; altura = {altura}")
    print(f"Área = {area}")

calcular_area(base, altura)#Parâmetro

calcular_area(1, 10)#Argumento
calcular_area(5, 25)#Argumento

