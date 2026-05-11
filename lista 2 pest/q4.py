#q4
n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
n3 = int(input("Digite n3: "))

if n1 == n2 and n1 == n3 and n3 == n2:
    soma = (n1 + n2 + n3)
    mult = soma*3
    print(f"Resultado = {mult}")

else:
    print(f"Resultado = {n1 + n2 + n3}")