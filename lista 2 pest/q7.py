#q7
num = int(input("Digite um número de 4 dígitos:"))
d1 = (num // 1000) % 10
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = (num % 10)

if d2 == d3 and d1 == d4:
    print("Os números são espelhos")
else:
    print("Os números não são espelhos")