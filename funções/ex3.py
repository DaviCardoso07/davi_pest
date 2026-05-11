def calcular_area_ret(base, altura):
    area = base * altura
    return area

def calcular_area_quad(lado):
    area = lado**2
    return area

A1 = calcular_area_ret(1, 4)
A2 = calcular_area_ret(5, 1)
A3 = calcular_area_ret(1, 3)
A4 = calcular_area_quad(2)

area_final = A1 + A2 + A3 + A4 

print(f"A área final é {area_final}")


