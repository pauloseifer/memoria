#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

escolas = [
"31345415",
"31108804",
"31108812",
"31108821",
"31108863",
"31108880",
"31108901",
"31108839",
"31108847",
"31108855",
"31108961",
"31108979",
"31108952",
"31353205",
"31220663",
"31236381",
"31108936",
"31249246",
"31112844",
"31112615",
"31112623",
"31112631",
"31112640",
"31112747",
"31112755",
"31112275",
"31112291",
"31112496",
"31108944",
"31347256",
"31220833",
"31208329",
"31228141",
"31228150",
"31327549"]

opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--headless")
opcoes.add_argument("--window-size=1325x744")

driver = webdriver.Chrome("/home/pseifer/Downloads/chromedriver", chrome_options=opcoes)
acao = ActionChains(driver)

ideb = open("ideb.csv", "a")
ideb.write("escola;nível;ano;meta;nota\n")

for escola in escolas: 
  print("Escola: " + escola)
  driver.get("http://idebescola.inep.gov.br/ideb/escola/dadosEscola/" + escola)
  
  elemento = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]')
  time.sleep(2)
  print('1')
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(2) 
  elemento.click()
  time.sleep(2)
  print('2')
  
  for i in range(3, 11):
    periodo = ''
    try:  
      periodo = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/h2[1]').text
    except NoSuchElementException:
      break
    linha = escola + ';' + periodo
    for j in  range(1, 4):                  
      try: 
        linha = linha + ';'  
        linha = linha + driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/table[3]/tbody/tr[' + str(i) + ']/td[' + str(j) + ']').text
      except NoSuchElementException:
        break
    linha = linha + '\n'
    ideb.write(linha)

  for i in range(3, 11):
    periodo = ''
    try:  
      periodo = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/h2[2]').text
    except NoSuchElementException:
      break
    linha = escola + ';' + periodo
    for j in  range(1, 4):                  
      try:
        linha = linha + ';'    
        linha = linha + driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/table[6]/tbody/tr[' + str(i) + ']/td[' + str(j) + ']').text      
      except NoSuchElementException:
        break
    linha = linha + '\n'
    ideb.write(linha)

  for i in range(3, 11):
    periodo = ''
    try: 
      periodo = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/h2[3]').text
    except NoSuchElementException:
      break
    linha = escola + ';' + periodo
    for j in  range(1, 4):                  
      try: 
        linha = linha + ';'  
        linha = linha + driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[4]/div[7]/div[2]/div[1]/table[9]/tbody/tr[' + str(i) + ']/td[' + str(j) + ']').text
      except NoSuchElementException:
        break
    linha = linha + '\n'
    ideb.write(linha)

ideb.close()
driver.close()
