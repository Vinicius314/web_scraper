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
 

## 📂 Estrutura

```
web_scraper\
  ├── scraper.py
  ├── main.py
  ├── requirements.txt
  ├── README.md
  └── data\
        ├── quotes.csv
        └── imagens\
```

## 🛠️ Tecnologias utilizadas

- Python 3.x
- `requests` – Para requisições HTTP
- `BeautifulSoup` – Para parsing HTML
- `pandas` – Para estruturação e exportação dos dados


## ▶️ Como usar

1. Instale o Playwright:
```bash
pip install playwright
playwright install
```

2. Execute:
```
python scraper.py
```
