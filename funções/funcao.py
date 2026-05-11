#Função

#Já trabalhamos com função, tipo print, input e etc;

#O que diferencia isso das outras é que eu posso criar a minha própria e depois usada sempre;

#Isso deixa várias coisas mais intuitivas, ele basicamente faz as coisas que eu mando;

#Usamos o "def" para definir uma função;

#Os nomes das funções obedecem as mesmas regras das variáveis;

#parametros :valores necessários para a execucção, fica entre "()", são opcionais. Só vai precisar se for necessário por exemplo o nome dito anteriormente

def cartao_de_visitas():
    print("Olá, amigo")
    print("Meu nome é Davi Cardoso")
    print("Eu tenho 16 anos")
    print("Fortaleza > Ceará")

cartao_de_visitas()

#Exemplo de parâmetro:

nome = input("Digite seu nome: ")

def boas_vindas(nome):
    print(f"Seja bem vindo {nome}!!!")

boas_vindas(nome)

#Contexto global e contexto local

#O contexto global ele é definido tipo em uma variável, é meio que permanente;

#O local é o que está dentro da função, é o parâmetro

#Exemplo de uso de parâmetro:

param = "joão"

print(f"Antes da função: {param}")

def saudacao(param):
    print(f"Oi, {param}")

print(f"Depos da função: {param}")

aluno1 = "Gaspar"
aluno2 = "Caio"
aluno3 = "Davi"
aluno4 = "Matheus"

saudacao(aluno1)
saudacao(aluno2)
saudacao(aluno3)
saudacao(aluno4)


print(f"Depos de tudo: {param}")

#Parâmetro x argumento:

#Os argumentos preenchem os parâmetros, são de fora;

#Ex:

def saudacao(param):
    print(f"Seu nome {param}")

saudacao("Maria")



