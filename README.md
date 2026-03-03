# Análise e Predição de Filmes 🎬📊

Este projeto é um pipeline completo de ciência de dados e engenharia de dados que extrai dados de filmes da [API The Movie Database (TMDB)](https://www.themoviedb.org/), armazena-os em um banco de dados SQLite local e realiza análises estatísticas para explorar e prever as receitas e avaliações dos filmes.

## 🎯 Objetivo
O objetivo principal do estudo é investigar se a avaliação média e a receita de um filme podem ser explicadas ou previstas usando modelos de regressão linear simples e múltipla com base em características como orçamento (budget), duração (runtime) e popularidade.

## 📂 Estrutura do Projeto
- **`main.py`**: O script de ingestão de dados. Ele se conecta à API do TMDB, busca filmes lançados entre 2016 e 2026 e os salva em lotes no banco de dados.
- **`database.py`**: Gerencia o banco de dados SQLite local (`movies.db`), incluindo a criação de tabelas, inserção de dados e recuperação em lotes.
- **`movies_analysis.ipynb`**: O Jupyter Notebook principal contendo a Análise Exploratória de Dados (EDA), transformações de dados (ex: escala logarítmica) e modelagem de regressão usando `statsmodels`.
- **`verify_db.py` & `check_db.py`**: Scripts utilitários para testar a integridade do banco de dados e verificar os registros armazenados.
- **`environment.yml` & `requirements.txt`**: Arquivos de configuração de ambiente contendo todas as dependências necessárias para executar o projeto.
- **`.env`**: Contém a `API_KEY` para autenticação com a API do TMDB (precisa ser criado pelo usuário).

## 🚀 Como Começar

### Pré-requisitos
Certifique-se de ter o [Conda](https://docs.conda.io/en/latest/) instalado em seu sistema.

### Instalação
1. **Navegue até o diretório do projeto**:
   ```bash
   cd movies_analysis
   ```

2. **Configure o ambiente**:
   Use o `environment.yml` fornecido para criar um ambiente Conda com todas as bibliotecas científicas necessárias (pandas, numpy, statsmodels, scikit-learn, etc.).
   ```bash
   conda env create -f environment.yml
   conda activate movies_analysis
   ```

3. **Configure a Chave da API (API Key)**:
   Crie um arquivo `.env` no diretório raiz e adicione seu token de acesso de leitura da API do TMDB:
   ```env
   API_KEY=sua_chave_da_api_tmdb_aqui
   ```

### Uso
1. **Buscar Dados**:
   Execute o script principal para começar a baixar dados de filmes da API para o seu banco de dados SQLite local.
   ```bash
   python main.py
   ```

2. **Verificar Banco de Dados (Opcional)**:
   Você pode verificar se o banco de dados foi preenchido corretamente executando:
   ```bash
   python verify_db.py
   python check_db.py
   ```

3. **Executar a Análise**:
   Abra o Jupyter Notebook para visualizar ou executar os modelos de regressão.
   ```bash
   jupyter lab movies_analysis.ipynb
   ```

## 🛠️ Tecnologias Utilizadas
- **Linguagem**: Python 3.13
- **Coleta de Dados**: `requests`, API TMDB
- **Banco de Dados**: SQLite3
- **Manipulação de Dados**: `pandas`, `numpy`
- **Modelagem Estatística**: `statsmodels`, `scipy`, `scikit-learn`
- **Visualização de Dados**: `matplotlib`, `seaborn`
