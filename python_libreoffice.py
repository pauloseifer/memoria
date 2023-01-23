#! /usr/bin/env python3

## Escreve texto no docs
## Extraído de https://gist.github.com/Foadsf/58d401c9b9ed5d80f60deee88d1fcdfd
##
## ATENÇÃO!!!
##
## A inicialização do writer tem que ser feita assim:
## /usr/bin/soffice --impress --norestore --nologo --norestore --nofirststartwizard --accept="socket,port=2002;urp;"
## e não da forma como é indicada no artigo

import uno

## DESCOMENTAR PARA TESTAR A PARTE DE TEXTO

## localContext = uno.getComponentContext()
## resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext)
## context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
## desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
## model = desktop.getCurrentComponent()
## text = model.Text
## cursor = text.createTextCursor()
## text.insertString(cursor, 'Hello world!', 0)



## Este trecho foi retirado de
## http://christopher5106.github.io/office/2015/12/06/openoffice-libreoffice-automate-your-office-tasks-with-python-macros.html
## que é referenciado no artigo anterior
##
## O código mexe com o calc
##
## Ver também: https://wiki.documentfoundation.org/Macros/Python_Guide/Calc/Calc_sheets

## /usr/bin/soffice --calc --norestore --nologo --norestore --nofirststartwizard --accept="socket,port=2002;urp;"

## get the uno component context from the PyUNO runtime
#localContext = uno.getComponentContext()
#
## create the UnoUrlResolver
#resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext )
#
## connect to the running office
#ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
#smgr = ctx.ServiceManager
#
## get the central desktop object
#desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
#
## access the current writer document
#model = desktop.getCurrentComponent()
#
## Lista o nome das planilhas
#nomes = model.Sheets.ElementNames;
#print(nomes)
#
## access the active sheet
#active_sheet = model.CurrentController.ActiveSheet
#
## access cell C4
#cell1 = active_sheet.getCellRangeByName("C4")
#
## set text inside
#cell1.String = "Hello world"
#
## other example with a value
#cell2 = active_sheet.getCellRangeByName("E6")
#cell2.Value = cell2.Value + 1

##########
##
## Este trecho foi criado por chatBot para inserir uma imagem em um slide
##
## Adaptei a inicialização para pelo código anterior
##
##########

# get the uno component context from the PyUNO runtime
localContext = uno.getComponentContext()

# create the UnoUrlResolver
resolver = localContext.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", localContext )

# connect to the running office
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
smgr = ctx.ServiceManager

# get the central desktop object
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)

# access the current writer document
document = desktop.getCurrentComponent()

# A partir daqui o código é do chatbot

from com.sun.star.beans import PropertyValue
from com.sun.star.awt import Size
from com.sun.star.awt import Point

# Get the current slide
slide = document.CurrentController.CurrentPage
#indice = slide.getIndex()

import urllib.parse ## 

# Create a graphic object with the desired image file
graphic = document.createInstance("com.sun.star.drawing.GraphicObjectShape")
graphic.GraphicURL = "file:////home/pseifer/repoprogs/memoria/chauvetpansm.jpg"

# Set the size and position of the image on the slide
tamanho = Size()
tamanho.Height = 429*10
tamanho.Width = 1003*10
posicao = Point()
posicao.X = 100
posicao.Y = 100
graphic.Size = tamanho
graphic.Position = posicao

slide.add(graphic)
