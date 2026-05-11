#fatiamento(slicing) de strings:
#eu pego um pedaço uma parte da string, você pra isso usa basicamente um intervalo
#fatiar uma string é fazer uma cópia de uma parte da string. 
#Essa cópia é feira através de um intervalo definido entre colchetes.

nome = "Francisco"
#       012345678

print(f"início ao fim: {nome[0:4]}") 
#ele n pega o ultimo caractere, ent ele vai printar "Fran"

print(f"intervalo: {nome[4:]}")
 #deixar dps dos : em branco significa até o final do numero, nesse caso "cisco"

print(f"intervalo: {nome[ : ]}") 
#ele vai entender que é do início ao fim

print(f"intervalo com passo {nome[1:7:2]}") 
#essa parte do final agr significa que ele vai ficar variando de 2 em 2 até o 7 

print(f"intervalo com passo {nome[ : : ]}") 
#Vai entender o padrão, início até o fim variando de 1 em 1

print(f"intervalo com passo negativo {nome [ : :-1]}")
#Vai começar do final e indo de um em 1, printando assim o nome invertido

