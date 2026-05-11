#q5
num = int(input("Digite um número: "))
num2 = num +1
cont = 0
soma = 0
for i in range(1, num2, 1):
    cont = cont+ 1
    if num % cont == 0 and cont != num:
        soma = cont + soma
        if soma == num:
            print("Número perfeito")
          
if soma != num:           
    print("Número não é perfeito")