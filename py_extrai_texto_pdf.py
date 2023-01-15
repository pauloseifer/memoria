#! /bin/env python3

# Código em python para extração dos dados dos índice básicos
# relativos aos módulos fiscais de propriedades rurais.
# O texto foi inserido aqui a partir do history do console do python3
# sem verificação.
#
# Cada linha foi lida como um bloco, senão o texto extraído sairia com
# uma célula da tabela por linha.
# O resto de edição e eliminação de texto não pertinente foi feito no
# excel.

import fitz

doc = fitz.open("indices_basicos_2013_por_municipio.pdf")

final = open("teste.csv", "w")

for pagina in doc:
#  for bloco in pagina.get_text("blocks")[19:-1]:
  for bloco in pagina.get_text("blocks"):
    final.write(bloco[4].replace('\n', '\t')[0:-1])
    final.write('\n')
final.close()
