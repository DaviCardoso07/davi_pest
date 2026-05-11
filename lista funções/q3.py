def conversor_moedas(real : float, taxa : float):
    dolar = real * taxa
    return f"a conversão deu {dolar} dólares"

real = float(input("Digite um valor em real: "))
taxa = float(input("Digite a taxa de câmbio: "))

conversor_moedas(real, taxa)

result = conversor_moedas(real = real, taxa =  taxa)

print(result)
   

