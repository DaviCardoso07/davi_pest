#q3
num = int(input("Digite um número: "))
soma = 0
for mult in range(0, num, 1):
    if mult % 3 == 0:
        soma = soma + mult
        print(mult)

print(f"a soma dos múltiplos de 3 foi {soma}")  
    
