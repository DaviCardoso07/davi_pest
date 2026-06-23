#q17
L = []
while True:
    acao = input("Digite o número que você deseja adicionar, caso queira sair, digite('sair'): ")
    if acao.isdigit():
        acao = int(acao) 
        if len(L) == 0:
            L.insert(0, acao)
        else:
            for i in range(len(L)):
                L.insert(i, acao)
    elif acao == "sair":
        break
    else:
        print("Nome inválido, tente novamente")

print(L)