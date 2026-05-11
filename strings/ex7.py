def pega_str(str1 : str, str2 : str):
    char1 = str1[0]
    char2 = str2[-1]
    result = char1 + char2
    return result

string1 = input("Digite uma palavra: ")
string2 = input("Digite uma palavra: ")

print(pega_str(str1 = string1, str2 = string2))