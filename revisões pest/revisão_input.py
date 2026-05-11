#input(como se fosse um "leia") tipo assim, "variável leia isso daqui: "

nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")#percebe-se que falta o "int", então o código vai dar um valor errado, ele vai repetir a idade 2 vezes

dobro_idade = idade * 2

print(nome)
print(f"Daqui a {idade} anos você terá {dobro_idade} anos.")

#cast: mudar a condição de um valor, tipo o int, que transforma o dado em inteiro por exemplo 

x = int(2.67) 
y = float(2)
z = str(3)
