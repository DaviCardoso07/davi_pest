
def calculadora_simples(num1 : float, num2 : float, op : str):
    if op == "soma":
        result = num1 + num2
    elif op == "subtracao":
        result = num1 - num2
    elif op == "multiplicacao":
        result = num1 * num2
    elif op == "divisao":
        result = num1 / num2

    return result


num1 = float(input("Digite num1: "))
num2 = float(input("Digite num2: "))
op = input("Digite a operação desejada (soma, subtracao, multiplicacao, divisao): ")

print(calculadora_simples(num1 = num1 , num1 = num2, op = op ))

   