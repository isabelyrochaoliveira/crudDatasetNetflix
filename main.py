from functions import inserirFilme, removerFilme, atualizarFilme, listarTodosFilmes, listarTodosFilmesCategoria, listarTodosFilmesCrescente

from utils import existeArquivo, leArquivo, lerInt, salvarArquivo

from relatorio import gerarRelatorio


def menu(dic_netflix):
    
    opcoes = ("\n-------------------------- MENU --------------------------\n"
          "\n1 - Inserir novo filme/série"
          "\n2 - Remover filme/série"
          "\n3 - Atualizar filme/série"
          "\n4 - Listar todos os filmes/séries"
          "\n5 - Listar todos os filmes/séries em ordem crescente"
          "\n6 - Listar todos os filmes/séries de uma categoria"
          "\n0 - Sair\n")
    
    print(opcoes)

    opc = lerInt("\nEscolha uma opção: ")

    while opc != 0:
        if opc == 1:
            inserirFilme(dic_netflix)

        elif opc == 2:
            removerFilme(dic_netflix)

        elif opc == 3:
            atualizarFilme(dic_netflix)

        elif opc == 4:
            listarTodosFilmes(dic_netflix)

        elif opc == 5:
            listarTodosFilmesCrescente(dic_netflix)

        elif opc == 6:
            listarTodosFilmesCategoria(dic_netflix)

        else:
            print("\nOpção inválida!\n")

        print(opcoes)

        opc = lerInt("\nEscolha uma opção: ")

#=====================================================================

dic_netflix = {}

if existeArquivo('netflix_titles.csv'):
    leArquivo(dic_netflix)

menu(dic_netflix)

salvarArquivo(dic_netflix)

gerarRelatorio(dic_netflix)

print("\nPrograma finalizado!\n")