#Crie um programa para ler um número inteiro N e escrever o dobro desse número na tela
N = int(input("Digite um número inteiro: "))

res = N * 2

print(res)
#Faz esse código ai
num_termos = int(input("Quantos termos? "))

n1 = 0
n2 = 1
cont = 0

if num_termos == 1:
    print(n1)
else:
    while cont < num_termos:
        print(n1)
        prox = n1 + n2
        n1 = n2 
        n2 = prox
        cont +=1
#Identifique o erro desse código
i = 1
while i % 7 != 0:
    print(i)
    i += 1
    if i % 7 == 0:
        print(i)

print("Encontrado")
#Identifique o erro desse código:
num = int(input("Digite um número inteiro: "))
fat = 1

if num<0:
    print("Número inválido")
else:
    while num >= 0 :
        if num == 0:
            print(f"Fatorial: {fat}")
            num -= 1
        else:
            fat *= num
            num -= 1
