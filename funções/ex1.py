nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

def calculo_idade(nome,idade):
    print(f"nome = {nome}; idade = {idade + 1} ")
    print(f"{nome} ano que vem você terá {idade + 1} anos")

calculo_idade(nome,idade)#Parâmetro
    
calculo_idade("Matheus", 21)#Argumento

