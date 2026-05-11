#q2
idade = int(input("Digite sua idade: "))

if idade >=60:
    print("Idoso")
elif idade >=18 and idade <60:
    print("Adulto")
elif idade >=12 and idade <18:
    print("Adolescente")
else:
    print("Criança")