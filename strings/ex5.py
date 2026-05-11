string1 = input("Digite a primeira string: ")
string2 = input("Digite a primeira string: ")

print(f"Primeiro caractere {string1[0]}")
print(f"Primeiro caractere {string2[0]}")

string1[0] = string2[0] #Vai dar erro, porque a STRING É IMUTÁVEL