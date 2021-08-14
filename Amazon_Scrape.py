import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = 'https://www.amazon.com.br'
produto = 'iphone'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path=r"C:\workspace\newproject\chromedriver.exe")
driver.maximize_window()
driver.get(url)
driver.find_element_by_id("twotabsearchtextbox").send_keys(produto + Keys.RETURN)
url = ('https://www.amazon.com.br/s?k=' + produto + '&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss')
pagina = requests.post(url, headers=headers)
driver.quit()
pagina.raise_for_status()


soup = BeautifulSoup(pagina.content, "html.parser")
itens = soup.find_all('h2', class_= 'a-size-mini a-spacing-none a-color-base s-line-clamp-4')
precos = soup.find_all('div', class_='a-row a-size-base a-color-base')
ultima_pagina = soup.find('div', class_='a-section a-spacing-small a-spacing-top-small').get_text()
quantidade = ultima_pagina[3:5]


for r in range(0,int(quantidade)):
    item = itens[r]
    preco = precos[r]
    titulo = item.find('span', class_='a-size-base-plus a-color-base a-text-normal').get_text()
    valor = preco.find('span', class_='a-offscreen').get_text()
    
    with open (produto + '_amazon.csv', 'a', newline='',encoding='UTF-8') as f:
            linha = titulo + ';' + valor + '\n'
            f.write(linha)