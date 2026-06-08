#fatiamento:
#a mesma coisa de str
L = [1, 1, 2, 3, 4,'aula', True]

print(L[::-1])
print(L[2:4])

#Vamos trabalhar com o CRUD(create,read,update e delete) -> adicionar, ler(printar), atualizar e deletar
#estavamos vendo o update
L = [1,2]
L[0] = 10

#MÉTODOS DE ADIÇÃO DE ELEMENTOS NA LISTA:
#1) append - adiciona o elemento ao FINAL da lista
L = [1,2]
L.append('a') #add o "a" na lista, meio que no final da lista
print(L)

#2) insert - adiciona um elemento em uma parte da lista
#ao adicionar o elemento meio que ele toma o espaço de um elemento que estiver no lugar, 
#e os elementos seguintes mudam de lugar

L = ['a', 'b']
L.insert(1, 'fortaleza')
print(L)
#o 1° é a posição e o 2° é o caractere que vc quer adicionar

# MÉTODOS DE REMOÇÃO DE ELEMENTOS NA LISTA:
# 1) remove - Remove um elemento específico da lista(O primeiro que ele achar)

L = [2, 2, 3, 4]
L.remove(2)# removeu, nesse caso o primeiro 2 que ele achou
print(L)

# 2) pop - remove o elemento do índice:
L = [2, 2, 3, 4]

L.pop(2) #remove o elemento do índice indicado, nesse caso o 3

print(L)