#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import re
import time



opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--headless")
opcoes.add_argument("--window-size=1325x744")

driver = webdriver.Chrome("/home/pseifer/lib/chromedriver/chromedriver", chrome_options=opcoes)
driver.get("https://aplicacoes.cidadania.gov.br/ri/pabcad/index.html")

municipios = open("/home/pseifer/tmp/Regina/renda/municipios.csv", "r")
lista = municipios.read().split()

cadunico = open("/home/pseifer/tmp/Regina/renda/cadunico.csv", "a")
cadunico.write("municipio; Familias no AB; total repassado no AB; Benefício médio no AB; Famílias no CadUnico; Fam Cadastro Atualizado; Renda até meio SM; Renda até meio SM com Cadastro Atualizado\n")

erro = open("/home/pseifer/tmp/Regina/renda/erro.log", "a")

for i in range(len(lista)): 
  UF = lista[i][:2]

## linha = lista[i]
  print(lista[i])  
  selecao = Select(driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[1]/select'))
  selecao.select_by_value(UF)
  
  time.sleep(5)
  selecao = Select(driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[3]/div/div/form/div[1]/div[2]/div/select'))

  selecao.select_by_value(lista[i])
  
  driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[3]/div/div/form/div[2]/div/button').click()
  driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/div[1]/div/div[2]/button').click()
  
  time.sleep(30)

  try:
    linha = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div[1]/h1").text
    
    texto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div[1]/p[8]').text
    numeros = re.findall('[0-9.,]*[0-9]+', texto)
    linha = linha + ";" + numeros[1] + ";" +numeros[2] + ";" + numeros[3] 
    
    texto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[1]/p/strong[1]').text
    numeros = re.findall('[0-9.,]*[0-9]+', texto)
    linha = linha + ";" + numeros[0]
    
    texto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[2]/p/strong[1]').text
    linha = linha + ";" + texto
    
    texto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[3]/p/strong[1]').text
    linha = linha + ";" + texto
      
    texto = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/div[2]/div/div[3]/ul/li[4]/p/strong[1]').text
    linha = linha + ";" + texto + "\n"
  
    cadunico.write(linha)
    driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div[1]/a').click()

    print(" foi")

  except NoSuchElementException:
    erro.write(lista[i] + " demorou\n")
    driver.get("https://aplicacoes.cidadania.gov.br/ri/pabcad/index.html")
    print(" não foi") 
  
cadunico.close()
erro.close()
municipios.close()
driver.close()
