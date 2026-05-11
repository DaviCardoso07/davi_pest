print(type(1))#int
print(type("1"))#string
print(type(1.0))#float
print(type('1.0'))#string
print(type([1]))#list(vamos ver dps)
print(type((1,0)))#tupla(vamos ver dps)
print(type({1}))#set(conjunto)[não vamos ver nessa disciplina]
print(type({1:1}))#dict(dicionário)[só no final dessa disciplina]
print(type(True))#Booleano

#nomes de variáveis

#não pode usar "hifen" o "-", nesse caso use o "_"
#não pode começar com número
#não pode começar com palaras reservadas, tipo "if" e etc

nome = 'davi'

print(f"{nome:.^10}") #...davi...
print(f"{nome:@<10}") # davi@@@@@
print(f"{nome:!>10}") # !!!!!!davi    

#regra -> {variável} {preenchimento} {tamanho} [acho que é assim]

#simbolos:

#/ -> divisão comum
#// -> número inteiro que divide o número(sem usar a vírgula)
#% -> resto da divisão

#operador lógico not -> ele diz que uma afirmação está errada