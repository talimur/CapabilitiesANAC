import requests
import lxml
import pprint
from bs4 import BeautifulSoup
#import pandas as pd

# site a ser iterado https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=0000000001 to 0000001500


def webscraper():
  i = 1
  x = 0
  dicio_fornecedores = {}
    #roda atraves dos numeros de fornecedor
  for i in range(i,3):
    
    pagina = requests.get(("https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=000000"+ str('%04d'%i)))
    print (i)
    #transforma página em objeto
    soup = BeautifulSoup(pagina.text, 'lxml')

    #separa as tabelas do arquivo
    tables = soup.findAll('table', width="710")

    #pega apenas os campos da tabela que tem atributos de texto
    tabela_basica = tables[3].findAll('font')

    #limpa as tags da tabela
    for tag in tabela_basica: 
      tag.attrs = None

    print (len(tabela_basica)) #teste para verificar a quantidade de itens na tabela
    
    #imprime a posição e cada item da posição na tabela
    nova_tabela = []
    for i in tabela_basica:
      nova_tabela.append((i.get_text("'", strip=True)))

    #adiciona a lista na posição do dicionário de acordo com o número do endereço do fornecedor
    dicio_fornecedores[x] = nova_tabela
    x+=1
    #print (tabela_basica)
    print ("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
  pprint.pprint(dicio_fornecedores)

webscraper()
