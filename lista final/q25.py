#q25
def menu(acao):
    print("------------------------------------")
    print("BANCO DE DADOS DE FILMES")
    print("------------------------------------")
    print("OPÇÕES:")
    print("0 - adicionar filmes")
    print("1 - pesquisar por gênero")
    print("2 - listar todos os filmes")
    print("3 - sair")
    acao = input("Digite oque você deseja fazer: ")
    return acao
def verifica_vazio(acao):
    if acao == '':
        while True:
            acao = input("Campo vazio, digite algo!!!")
    else:
        pass
    return acao
def adicionar_filmes(filme : list, titulo : list, diretor : list, ano : list, genero : list):
    add_t = input("Digite o titulo do filme que deseja adicionar: ").capitalize().strip()
    titulo.append(add_t)
    add_d = input("Digite o diretor do filme: ").capitalize().strip()
    diretor.append(add_d)
    add_a = input("Digite o ano do filme: ").strip()
    ano.append(add_a)
    add_g = input("Digite o gênero do filme: ").upper().strip()
    genero.append(add_g)

    filme.insert(0, titulo)
    filme.insert(1, diretor)
    filme.insert(2, ano)
    filme.insert(3, genero)

    return filme

def procura_genero(filme):
    proc = input("Digite o gênero do filme que deseja achar: ").upper().strip()
    var = 0
    for i in range(len(filme[3])):
        if filme[3][i] == proc:
            print(filme)
            print(f"título: {filme[0][i]}")
            print(f"diretor: {filme[1][i]}")
            print(f"ano: {filme[2][i]}")
            print(f"gênero: {filme[3][i]}")
                
            var += 1
    if var == 0:
        print("Gênero do filme não encontrado")
        



    
filme = []
titulo = []
diretor = []
ano = []
genero = []
opcao = ''
while True:
    opcao = menu(acao = opcao)
    if opcao == "0":
        filme = adicionar_filmes(filme = filme, titulo = titulo, diretor = diretor, ano = ano, genero = genero)
        print(genero)
    elif opcao == "1":
        procura_genero(filme = filme)
    elif opcao == "2":
         for i in range(len(filme)):
            print(f"título: {filme[0][i]}")
            print(f"diretor: {filme[1][i]}")
            print(f"ano: {filme[2][i]}")
            print(f"gênero: {filme[3][i]}")
    elif opcao == "3":
        break