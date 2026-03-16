from utils import lerTexto, filmeExiste

def inserirFilme(dic_netflix):

    print("\n--------INSERIR FILME/SÉRIE--------\n")

    titulo = lerTexto("Título: ")

    if filmeExiste(dic_netflix, titulo):
        print("\nEsse título já existe!\n")
        return

    tipo = lerTexto("Tipo (Movie/TV Show): ")
    pais = lerTexto("País: ")
    adicionado = lerTexto("Data adicionada: ")
    ano = lerTexto("Ano de lançamento: ")
    duracao = lerTexto("Duração: ")
    categorias = lerTexto("Categorias: ")

    dic_netflix[titulo] = {
        "tipo": tipo,
        "pais": pais,
        "adicionadoEm": adicionado,
        "ano": ano,
        "duracao": duracao,
        "categorias": categorias,
    }

    print("\nFilme/série inserido com sucesso!\n")

#=====================================================================

def removerFilme(dic_netflix):

    print("\n--------REMOVER FILME/SÉRIE--------\n")

    titulo = lerTexto("Título: ")

    if not filmeExiste(dic_netflix, titulo):
        print("\nEsse título não foi encontrado!\n")
        return
    
    else:
        del dic_netflix[titulo]
        print("\nFilme removido com sucesso!")

#=====================================================================

def atualizarFilme(dic_netflix):

    print("\n--------ATUALIZAR FILME/SÉRIE--------\n")

    titulo = lerTexto("Título: ")

    if not filmeExiste(dic_netflix, titulo):
        print("\nEsse título não foi encontrado!\n")
        return

    filme = dic_netflix[titulo]

    print("\nPressione ENTER para manter o valor atual.\n")

    novoTipo = input(f"Tipo ({filme['tipo']}): ")
    if novoTipo.strip() != "":
        filme["tipo"] = novoTipo

    novoPais = input(f"País ({filme['pais']}): ")
    if novoPais.strip() != "":
        filme["pais"] = novoPais

    novaData = input(f"Adicionado em ({filme['adicionadoEm']}): ")
    if novaData.strip() != "":
        filme["adicionadoEm"] = novaData

    novoAno = input(f"Ano ({filme['ano']}): ")
    if novoAno.strip() != "":
        filme["ano"] = novoAno

    novaDuracao = input(f"Duração ({filme['duracao']}): ")
    if novaDuracao.strip() != "":
        filme["duracao"] = novaDuracao

    novaCategoria = input(f"Categorias ({filme['categorias']}): ")
    if novaCategoria.strip() != "":
        filme["categorias"] = novaCategoria

    print("\nFilme/série atualizado com sucesso!\n")

#=====================================================================

def listarTodosFilmes(dic_netflix):

    print("\n--------LISTAR TODOS OS FILMES/SÉRIES--------\n")

    contador = 0

    for titulo, dados in dic_netflix.items():
        print("\n------------------------------------------------------------\n")
        print(f"Título: {titulo}")
        print(f"Tipo: {dados['tipo']}")
        print(f"País: {dados['pais']}")
        print(f"Adicionado em: {dados['adicionadoEm']}")
        print(f"Ano: {dados['ano']}")
        print(f"Duração: {dados['duracao']}")
        print(f"Categorias: {dados['categorias']}")

        contador += 1

        if contador == 15:
            print("\n")
            break

#=====================================================================

def listarTodosFilmesCrescente(dic_netflix):

    print("\n--------LISTAR TODOS OS FILMES/SÉRIES EM ORDEM CRESCENTE--------\n")

    contador = 0

    ordenados = sorted(dic_netflix.items(), key=lambda x: x[0])

    for titulo, dados in ordenados:
        print("\n------------------------------------------------------------\n")
        print(f"Título: {titulo}")
        print(f"Tipo: {dados['tipo']}")
        print(f"País: {dados['pais']}")
        print(f"Adicionado em: {dados['adicionadoEm']}")
        print(f"Ano: {dados['ano']}")
        print(f"Duração: {dados['duracao']}")
        print(f"Categorias: {dados['categorias']}")

        contador += 1

        if contador == 15:
            print("\n")
            break

#=====================================================================

def listarTodosFilmesCategoria(dic_netflix):

    print("\n--------LISTAR TODOS OS FILMES/SÉRIES DE UMA CATEGORIA--------\n")

    filtro = input("Digite a categoria desejada: ").lower()

    encontrados = 0

    for titulo, dados in dic_netflix.items():
        
        if filtro in dados["categorias"].lower():
            print("\n------------------------------------------------------------\n")
            print(f"Título: {titulo}")
            print(f"Tipo: {dados['tipo']}")
            print(f"País: {dados['pais']}")
            print(f"Adicionado em: {dados['adicionadoEm']}")
            print(f"Ano: {dados['ano']}")
            print(f"Duração: {dados['duracao']}")
            print(f"Categorias: {dados['categorias']}")

            encontrados += 1

            if encontrados == 15:
                print("\n")
                break

    if encontrados == 0:
        print("\nNenhum filme encontrado nessa categoria.\n")