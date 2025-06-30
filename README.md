# Web Scraper

Este projeto tem como objetivo automatizar a coleta de informações de páginas web. Ele permite extrair dados estruturados como textos, links, imagens e tabelas de forma rápida e eficiente, salvando os resultados em arquivos CSV ou JSON.

## 🚀 Funcionalidades

- Coleta automática de dados a partir de URLs.
- Extração de informações como:
  - Títulos e descrições
  - Links e imagens
  - Tabelas e listas
- Exportação dos dados para:
  - `.csv`
  - `.json`

## 🛠️ Tecnologias utilizadas

- Python 3.x
- `requests` – Para requisições HTTP
- `BeautifulSoup` – Para parsing HTML
- `pandas` – Para estruturação e exportação dos dados

## 📁 Estrutura do Projeto

web_scraper/
-├── main.py # Script principal de execução
-├── scraper.py # Funções de scraping
-├── utils.py # Funções auxiliares (ex: limpeza de dados)
-├── requirements.txt # Bibliotecas necessárias
-├── README.md # Descrição do projeto
-└── output/ # Pasta com os resultados exportados


## ▶️ Como usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/web_scraper.git
   cd web_scraper
