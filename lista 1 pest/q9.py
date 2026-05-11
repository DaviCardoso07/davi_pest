#q9
x1 = int(input("Digite x1: "))
y1 = int(input("Digite y1: "))
x2 = int(input("Digite x2: "))
y2 = int(input("Digite y2: "))

dist_t = (x2-x1)**2 + (y2-y1)**2
dist_f = dist_t**0.5

print(f"a distância entre os dois pontos é de {dist_f}")