import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def download_images(url):
    # Faz o download da página HTML
    response = requests.get(url)
    if response.status_code == 200:
        # Cria uma pasta para armazenar as imagens
        if not os.path.exists('imagens'):
            os.makedirs('imagens')

        # Analisa o HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra todas as tags 'img'
        img_tags = soup.find_all('img')

        # Faz o download de cada imagem
        for img in img_tags:
            img_url = img['src']
            img_url = urllib.parse.urljoin(url, img_url)  # Resolve URLs relativos
            img_name = img_url.split('/')[-1]
            img_path = os.path.join('imagens', img_name)
            with open(img_path, 'wb') as img_file:
                img_file.write(requests.get(img_url).content)
                print(f'Imagem {img_name} baixada com sucesso!')

    else:
        print('Falha ao acessar a página.')

# Exemplo de uso
url = ''
download_images(url)
