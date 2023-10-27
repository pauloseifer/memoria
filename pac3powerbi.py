NÃO FOI EXECUTADO PROGRAMA. OS DADOS FORAM BAIXADOS DIRETAMENTE PELA SHELL DO PYTHON.
NA SEQUÊNCIA, UM DESCRITIVO DO QUE FOI UTILIZADO.

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
from selenium.webdriver.common.action_chains import ActionChains


Usei o firefox aberto, porque por algum motivo o chrome não funcionou, e queria ver o andamento da mudança na barra de seleção (não usei headless)
driver = webdriver.Firefox()

Identifiquei na página original do PAC a referência ao Power BI e abri o a referência direto no chrome. Funciona como uma página normal.
driver.get("https://app.powerbi.com/view?r=eyJrIjoiMmVmZDFkNDAtZTI1Ni00MjgwLWFmOWEtZjJiYzBmM2FkYmE4IiwidCI6IjFjYzNjNTA4LTAxYzctNDQ2MC1iZDJiLWFmZTk1ZTgwYjhhZiJ9")

Abri o arquivo.
pac3bruto = open("/home/pseifer/tmp/pac3bruto.csv", "a")

Das muitas tentativas, o que funcionou foi o seguinte:

def pega_dados():
   for i in range(12508):
      elemento = driver.find_element(By.XPATH, "//div[@row-index='" + str(i + 1)+ "']")
      linha = elemento.text
      linha = str(i) + ";" + linha.replace("\n", ";")
      pac3bruto.write(linha + "\n")
      celula = elemento.find_element(By.XPATH, ".//div[@column-index='3']")
      celula.send_keys(Keys.DOWN)

Fiz o código abaixo para pegar os dados de homicídios de https://app.powerbi.com/view?r=eyJrIjoiYjhhMDMxMTUtYjE3NC00ZjY5LWI5Y2EtZDljNzBlNDg2ZjVkIiwidCI6ImViMDkwNDIwLTQ0NGMtNDNmNy05MWYyLTRiOGRhNmJmZThlMSJ9
Houve algum problema com o prímeiro município, Acrelândia, por conta da indexação, mas no fim foi possível corrigir manualmente.
######def pega_dados():
######   for i in range(5575):
######     elemento = driver.find_element(By.XPATH, "//div[@row-index='" + str(i)+ "']")
######     linha = str(i);
######     estado = elemento.find_element(By.XPATH, ".//div[@aria-colindex='2']").text
######     municipio = elemento.find_element(By.XPATH, ".//div[@aria-colindex='3']").text
######     h2020 = elemento.find_element(By.XPATH, ".//div[@aria-colindex='4']").text
######     h2021 = elemento.find_element(By.XPATH, ".//div[@aria-colindex='5']").text
######     h2022 = elemento.find_element(By.XPATH, ".//div[@aria-colindex='6']").text
######     linha = linha+";"+estado+";"+municipio+";"+h2020+";"+h2021+";"+h2022+"\n"
######     celula = elemento.find_element(By.XPATH, ".//div[@column-index='4']")
######     celula.send_keys(Keys.DOWN)
######     arquivo.write(linha)
     

      
O que a função faz é baixar elemento por elemento, 'clicando' para baixo para seguir para o próximo elemento.
Como cada elemento tem um índice único para o bloco de dados, de acordo com a seleção nas caixas de diálogos (deixei como "Todos"), coloquei o índice na busca pelo row-index, que é a propriedade do div que indica a linha/elemento. Para aplicar a seta para baixo, procurei uma célula dentro daquele div, e apliquei o Key.DOWN. Notar que na busca dentro do div da célula tem um ".", que indica que a busca deve ser realizada a partir do ponto atual, que é o elemento. 

pac3bruto.close()

OUTRAS TENTATIVAS

Pega as ações
actions = ActionChains(driver)

Identifiquei a barra de rolagem.
barra = driver.find_element('xpath', '/html/body/div[1]/report-embed/div/div[1]/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[4]/div')
Usei um valor aleatório para mudança na barra. Isso implicou na repetição de valores.

for k in range(1000): 
  for j in range(15):
    linha = ""
    for i in range(7):
        linha = linha + ";" + driver.find_element('xpath', '/html/body/div[1]/report-embed/div/div[1]/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div['+str(j+1)+']/div/div/div['+str(i+2)+']').text
     print(linha)   
     pac3bruto2.write(linha + '\n')
   actions.click_and_hold(barra).move_by_offset(0, 1).release().perform()
   time.sleep(3)


Outra forma de fazer, que funcionou melhor, porque pega todos 'div' filhos do 'div' que tem a lista de obras.   
pai = driver.find_element('xpath', '/html/body/div[1]/report-embed/div/div[1]/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div')

def pega_dados():   
  for k in range(1000):
     print('oi')
     filhos = pai.find_elements(By.XPATH, '*')
     for j in range(len(filhos)):
       linha = ""
       for i in range(7):
         linha = linha + ";" + driver.find_element('xpath', '/html/body/div[1]/report-embed/div/div[1]/div/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[10]/transform/div/div[2]/div/visual-modern/div/div/div[2]/div[1]/div[2]/div/div['+str(j+1)+']/div/div/div['+str(i+2)+']').text
       pac3bruto4.write(linha + '\n')
     actions.click_and_hold(barra).move_by_offset(0, 5).release().perform()
     time.sleep(10)


actions.send_keyw('Keys.ARROW_DOWN').perform()
elemento = driver.find_element(By.XPATH, "//div[@row-index='8565']")

def pega_dados():
   for i in range(29):
      elemento = driver.find_element(By.XPATH, "//div[@row-index='" + str(i + 12481)+ "']")
      linha = elemento.text
      linha = str(i) + ";" + linha.replace("\n", ";")
      pac3bruto.write(linha + "\n")
      celula = elemento.find_element(By.XPATH, ".//div[@column-index='3']")
      celula.send_keys(Keys.DOWN)

def vai_ate_fim():
   for i in range(13000):
      elemento = driver.find_element(By.XPATH, "//div[@row-index='" + str(i + 1)+ "']")
      celula = elemento.find_element(By.XPATH, ".//div[@column-index='3']")
      celula.send_keys(Keys.DOWN)
