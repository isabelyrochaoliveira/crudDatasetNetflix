# 🎬 Netflix Data Manager

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Este projeto é um sistema de gestão e análise de dados desenvolvido em Python, utilizando como base o dataset público da Netflix (`netflix_titles.csv`). O software permite gerenciar o catálogo de filmes e séries, além de gerar relatórios estatísticos sobre o acervo.

---

### 📖 Funcionalidades
- **Gestão de Catálogo (CRUD):** Inserção, remoção, atualização e listagem de títulos.
- **Filtros Avançados:** Busca por categorias específicas e exibição de títulos em ordem alfabética.
- **Persistência de Dados:** Manipulação dinâmica de arquivos CSV para leitura e salvamento automático dos registros.
- **Módulo de Relatórios:** Geração de um arquivo `relatorio.csv` contendo:
    - Cálculos de **Média** e **Mediana** de anos de lançamento e duração.
    - Identificação de valores **Mínimos** e **Máximos**.
    - Estatísticas sobre a quantidade de categorias por título.

---

### 🛠️ Estrutura do Projeto
O código foi desenvolvido de forma modular para facilitar a manutenção:
* `main.py`: Ponto de entrada da aplicação e controle do menu principal.
* `functions.py`: Lógicas de manipulação do dicionário (Inserir, Listar, Remover).
* `utils.py`: Funções utilitárias para validação de entrada e manipulação de arquivos CSV.
* `relatorio.py`: Processamento matemático e exportação de estatísticas.
