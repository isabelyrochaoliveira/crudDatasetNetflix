import os
import csv

def filmeExiste(dic_netflix, nomeFilme):

    if nomeFilme in dic_netflix:
        return True
    
    else:
        return False
    
#=====================================================================
    
def existeArquivo(nomeArquivo):

    if os.path.exists(nomeArquivo):
        return True
    
    else:
        return False
    
#=====================================================================

def leArquivo(dic_netflix):

    with open("netflix_titles.csv", newline='', encoding="utf-8") as f:
        leitor = csv.reader(f)

        next(leitor)

        for linha in leitor:
            titulo = linha[2]
            categoria = linha[10]

            try:
                ano = int(linha[7])
            except:
                ano = None

            dic_netflix[titulo] = {
                "tipo": linha[1],
                "pais": linha[5],
                "adicionadoEm": linha[6],
                "ano": ano,
                "duracao": linha[9],
                "categorias": categoria,
            }

    print(f"\n{len(dic_netflix)} registros carregados.\n")

#=====================================================================

def lerInt(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip() == "":
            print("Digite um número válido!")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Digite um número válido!")

#=====================================================================

def lerTexto(mensagem):

    while True:
        entrada = input(mensagem)
        if entrada.strip() == "":
            print("Esse campo não pode ficar vazio!")
        else:
            return entrada

#=====================================================================

def salvarArquivo(dic_netflix):

    with open("netflix_titles.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)

        escritor.writerow([
            "show_id", "type", "title", "director", "cast", "country",
            "date_added", "release_year", "rating", "duration",
            "listed_in", "description"
        ])

        id_count = 1

        for titulo, dados in dic_netflix.items():

            escritor.writerow([
                id_count,
                dados["tipo"],
                titulo,
                "",
                "",
                dados["pais"],
                dados["adicionadoEm"],
                dados["ano"],
                "",
                dados["duracao"],
                dados["categorias"],
                ""
            ])

            id_count += 1

    print("\nArquivo atualizado com sucesso!\n")