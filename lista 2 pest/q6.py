#q6
num = int(input("Digite um número de 4 dígitos:"))
d1 = (num // 1000) % 10
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = (num % 10)

if d1!=d2 and d1!=d3 and d1!=d4 and d2!=d3 and d2!=d4 and d3!=d4:
    print("Os números são diferentes entre si")
else:
    print("Os números não são diferentes entre si")