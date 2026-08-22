#Métodos de strings:

#Basicamente são funções que foram criadas prontas para serem acessadas a hora que quise;
#Para defina uma string e chame ela e colocando o ponto no final:

var = "Abacaxi"
# var.(aparece um monte de opções)

#1. Upper() (todas os caracteres maiúsculo) lower(todos os caracteres em minusculo):

str = "Cena Oculta"
nova_str = str.upper()
print(nova_str)
print(str.lower())

#2 Split() (transforma todos os elementos da string em uma lista, separando pelo espaço, fazendo assim as substrings)
str = "Cena Oculta"
print(str.split())

#2.1 Se eu colocar parametros ele vai separar com base no que eu colocar
str = "Todo mundo odeia o John"
print(str.split('o'))

#3. join(): Junta elementos de uma lista em uma única string usando uma string como separador/juntador.

lista_de_palavras = ['Cena', 'Oculta']
separador = "-" #geito que eu quero separar
nova_string = separador.join(lista_de_palavras)
print(nova_string)

#4. capitalize() ele deixa a primeira letra maiúscula e as restantes minúsculas
str = "Convergentes Foi O Mais O ORIGINAL"
print(str.capitalize())

#5. replace(): Substitui um determinado trecho da string por outro
#o 1º parametro indica oque eu quero substituir, e o 2º parâmetro indica a frase que vai substituir

str = "Ceará melhor do Nordeste"

print(str.replace('Ceará', 'Fortaleza'))

#6. count(): Conta o número de vezes que determinado caractere aparece

str = "Abacaxi"
print(str.count('a'))

#7. find() e index(): ambos retornam o índice(em que caractere está oque eu pedi) da primeira ocorrência,

str = "Cena Oculta"
print(str.find('c')) #retorna "-1" quando não encontra(melhor)
print(str.index('c')) #Da erro quando não encontra

#8. isalnum(), basicamente ele vai retornar true se tiver letras ou números,
#se tiver espaço, ou qualquer outro caractere por exemplo, vai retornar false,
str = "CenaOculta"
print(str.isalnum())
