#é uma forma de indicar o tipo, ele é usado para facilitar o dev para fazer de melhor maneira o código
#é apenas visual

def xpto(A : str, B : int, C : float) -> int: #A setinha indica o retorno do código, os dois pontos ":"" indica o tipo do parâmetro
    return 0

xpto(10, 10, 10) #quando vc colocar o "()" ele vai avisar o tipo, para evitar confusões

def calcula_idade(nome : str, idade : int):
    aux = idade + 1
    print(f"{nome}, ano que vem você terá {aux} anos")

#parâmetros nomeados(não necessita estar na ordem)
calcula_idade(idade = 20, nome ="maria") #Você especificando, msm colocando ao contrário dá certo
calcula_idade(nome ="maria", idade = 20)

#parâmetros posicionais (como a gente tava fazendo antes)
calcula_idade("Davi", 16)

#valor padrão

def boas_vindas(nome : str = "pessoa"): #Ele define o valor padrão como "pessoa", caso escreva algo ele vai sobscrever, senão ele vai só colocar "pessoa"    
    print(f"Seja bem vindo {nome}!!!")

boas_vindas()

def calcula_idade(idade : int, nome : str = "Pessoa"): #o valor padrão fica sempre no final, a não ser que todos tiverem
    aux = idade + 1
    print(f"{nome}, ano que vem você terá {aux} anos")

calcula_idade(nome = "Maria", idade = 20)
calcula_idade()

#Variável de escopo local(dentro da função), só podem ser acessadas dentro da função, ou do if, while e etc, a não ser que use o return
#Ex:
def calcula_idade(idade : int, nome : str = "Pessoa"): #o valor padrão fica sempre no final, a não ser que todos tiverem
    aux = idade + 1 #aux é uma variável local
    print(f"{nome}, ano que vem você terá {aux} anos")

#Variável de escopo global (fora de qualquer coisa), pode ser acessada de qualquer local do código
def minha_funcao():
    var = 10
    print(var)
    print(x)

x = 20 #Variável global "x"
minha_funcao()

#Alterar uma variável global por uma local:

def minha_funcao():
    global x # Você está afirmando que o x que vai ser alterado sera o global
    x = 21
    x = x + 10
    print(x)

x = 21

minha_funcao() #Vai printar 31
print(x)
