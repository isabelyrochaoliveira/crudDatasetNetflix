import csv

def gerarRelatorio(dic_netflix):

    lista_anos = []
    lista_duracoes = []
    lista_qtd_categorias = []

    for titulo, dados in dic_netflix.items():

        try:
            ano = int(dados["ano"])
            lista_anos.append(ano)
        except:
            pass

        duracao = dados["duracao"].lower()
        if "min" in duracao:
            try:
                minutos = int(duracao.replace("min", "").strip())
                lista_duracoes.append(minutos)
            except:
                pass

        qtd = len(dados["categorias"].split(","))
        lista_qtd_categorias.append(qtd)

    estatisticas = {
        "Ano": lista_anos,
        "Duração (minutos)": lista_duracoes,
        "Quantidade de Categorias": lista_qtd_categorias
    }

    with open("relatorio.csv", "w", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)

        escritor.writerow(["coluna", "minimo", "maximo", "media", "mediana"])

        for nome_coluna, lista in estatisticas.items():

            if len(lista) == 0:
                escritor.writerow([nome_coluna, "sem dados", "", "", ""])
                continue

            minimo = min(lista)
            maximo = max(lista)
            media = sum(lista) / len(lista)
            med = mediana(lista)

            escritor.writerow([
                nome_coluna,
                minimo,
                maximo,
                f"{media:.2f}",
                med
            ])

    print("\nRelatório criado com sucesso!\n")


def mediana(lista):
        lista_ord = sorted(lista)
        n = len(lista_ord)
        if n % 2 == 1:
            return lista_ord[n // 2]
        return (lista_ord[n//2 - 1] + lista_ord[n//2]) / 2