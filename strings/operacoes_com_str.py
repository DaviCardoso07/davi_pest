# Acessando elementos

str = "Abacaxi"

for i in range(len(str)):
    print(i, str[i])

for caractere in str:
    print(caractere)

#operações com strings

#Soma(concatenação):

#ao somar uma string voce junta ela com outra.
#A string é imutável, uma vez criada ela não pode ser alterada.
#então para alterar alguma coisa, criamos outra variável e somo ela com outra string.

str = "Abacaxi"
str2 = "@" + "bacaxi"
print(str)
print(str2)


#Multiplicação:

#Ao multiplicar nós repetimos a string

str = "IFCE"
repeticao = str * 5

print(repeticao)