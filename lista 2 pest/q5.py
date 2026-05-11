#q5
num = int(input("Digite um número: "))

if num % 4 == 0 and num % 5 == 0:
    print("O número é divisível por 4 e por 5")
elif num % 4 == 0:
     print("O número é divisível por 4")
elif num % 5 == 0:
     print("O número é divisível por 5")
else:
     print("não é divisível por 4 ou 5")