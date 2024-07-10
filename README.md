# Web Scraping do Mercado Livre

Este é um script básico de web scraping que busca produtos com preço ativo no Mercado Livre e salva os links desses produtos em um arquivo de texto.

## Funcionalidades

- Busca produtos no Mercado Livre com base em um termo fornecido pelo usuário.
- Filtra os produtos que possuem informações de preço.
- Salva os links dos produtos com preço ativo em um arquivo `links.txt`.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `beautifulsoup4`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/Gabriel-Hernandess/WebScrapingMercadoLivre.git
   cd WebScrappingMercadoLivre

## Instale as Bibliotecas Necessárias
pip install requests beautifulsoup4

## Exemplo de Uso
Digite o título do item para buscar no Mercado Livre: iPhone 12
Foram encontrados 10 links com preço e foram salvos no arquivo 'links.txt'
