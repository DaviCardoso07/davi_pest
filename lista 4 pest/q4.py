
num = int(input("Digite um número: "))

mult = 1

for i in range(1, num+1, 1):
    mult = mult * i
    print(i)

print(mult)