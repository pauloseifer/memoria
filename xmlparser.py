# Programa feito em python para fazer o scrapping de um kml de pontos de uma pesquisa
# O kml foi descompactado para xml e, daí, os dados retirados seguindo o XPath apropriado

import xml.etree.ElementTree as ET

documento = ET.parse('') ## arquivo xml
 
raiz = documento.getroot()

print(raiz.tag)

arquivo = open("com_coord.txt", "w")

arquivo.write('Comunidade;X;Y\n')

for filho in raiz.findall('.//*[@schemaUrl="#S_Entrevistas_Domicilios_DDSSSSDDDDS"]'):
  comunidade = filho.find('.//*[@name="Comunidade"]')
  X = filho.find('.//*[@name="x"]')
  Y = filho.find('.//*[@name="y"]')
  arquivo.write(comunidade.text.encode('utf-8') + ";" + X.text + ";" + Y.text + "\n")
  
arquivo.close()
