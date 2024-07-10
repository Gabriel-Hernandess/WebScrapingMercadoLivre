import requests
from bs4 import BeautifulSoup

def buscar_mercado_livre(item_busca):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    # URL de busca no Mercado Livre
    url = f"https://lista.mercadolivre.com.br/{item_busca}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        produtos = soup.find_all('li', {'class': 'ui-search-layout__item'})
        
        links_produtos = []
        
        for produto in produtos:
            # Verifica se há informações de preço disponíveis
            preco = produto.find('span', {'class': 'andes-money-amount__fraction'})
            if preco:
                link = produto.find('a', {'class': 'ui-search-link'})
                if link and 'href' in link.attrs:
                    links_produtos.append(link['href'])
        
        return links_produtos
    else:
        print(f"Falha ao acessar o Mercado Livre: {response.status_code}")
        return []

while True:
    # Solicitar título do item para busca
    item_busca = input("Digite o título do item para buscar no Mercado Livre: ")

    # Nome do arquivo para salvar os links
    nome_arquivo = "links.txt"

    # Realiza a busca no Mercado Livre
    links = buscar_mercado_livre(item_busca)

    # Salva os links com preço no arquivo
    with open(nome_arquivo, 'w') as file:
        for link in links:
            file.write(link + '\n')

    print(f"Foram encontrados {len(links)} links com preço e foram salvos no arquivo '{nome_arquivo}'")