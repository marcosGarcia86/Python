# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Criar instância do navegador
browser = webdriver.Firefox()
browser.maximize_window()

# abrir página web
browser.get('https://elicitacao.com.br')

# encontra campos de usuário e senha
username = browser.find_element_by_name('nm_email_usuario')
password = browser.find_element_by_name('nm_usu_senha')

# insere usuário e senha
username.send_keys('admin@forseti.com.br')
password.send_keys('pert0shyx6ve')

# clica no botão logar
login_attempt = browser.find_element_by_xpath('//*[@type="submit"]')
login_attempt.submit()

# abre nova página
browser.get('https://elicitacao.com.br/licitacao-buscar')

numero = browser.find_element_by_name('nu_licitacao')
numero.send_keys('142018')

buscar = browser.find_element_by_xpath('//*[@class="busca-portal-form-botao"]')
buscar.submit()

elm = browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)

elm.send_keys(Keys.END)
time.sleep(5)

paginacao = browser.find_element_by_id('link_page_2')
click = browser.find_element_by_xpath('//li[@class="next"]')
buscar.submit()

elm.send_keys(Keys.END)
time.sleep(15)

'''
# Seleciono todos os elementos que possuem a class post
posts = browser.find_elements_by_class_name('post')

# Para cada post printar as informações
for post in posts:

    # O elemento `a` com a class `post-title`
    # contém todas as informações que queremos mostrar
    post_title = post.find_element_by_class_name('post-title')

    # `get_attribute` serve para extrair qualquer atributo do elemento
    post_link = post_title.get_attribute('href')

    # printar informações
    print ("Títutlo: {titulo}, \nLink: {link}".format(
        titulo=post_title.text,
        link=post_link
    ))
'''

# Fechar navegador
browser.quit()
