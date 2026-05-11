def calcular_area(base, altura):
    area = base * altura
    print(f"base = {base}; altura = {altura}")
    print(f"Área = {area}")
    return area #transforma a variável "area" no valor da funcao "calcular_area"

A1 = calcular_area(5, 8) #"A1" agora recebeu o valor da área do "calcular_area(5, 8)"
A2 = calcular_area(20, 7) #"A2" agora recebeu o valor da área do "calcular_area(20, 7)"

area_final = A1 + A2

print(f"Área final = {area_final}")
