import requests
import lxml
from bs4 import BeautifulSoup

# site a ser iterado https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=0000000001 to 0000001500

def scraper():
  i = 1

#roda atraves dos numeros de fornecedor
  for i in range(1,3):
    pagina = requests.get(("https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=000000"+ str('%04d'%i)))
  
#transforma página em objeto
  soup = BeautifulSoup(pagina.text, 'lxml')
#text = soup.get_text()
  

#separa as tabelas do arquivo
  tables = soup.findAll('table', width="710")
  
  print (len(tables)) #só teste para ver tamanho da tabela

#pega apenas os campos da tabela que tem atributos de texto
  tabela_basica = tables[3].findAll('font')

#limpa as tags da tabela
  for tag in tabela_basica.find(True): 
    tag.attrs = None
  

  print (len(tabela_basica)) #teste para verificar a quantidade de itens na tabela
 
  print ("///////////////////////////////") #divisor
#imprime a posição e cada item da posição na tabela
  for i in tabela_basica:
    texto = [i.text]
    print ('Posição: ' + str(texto.index(i)) + ' ' + str(i))
    
dicio_fornecedores = { i : tabela_basica[i] for i in range(0, len(tabela_basica) ) }
#print (tabela_basica)
#print ("///////////////////////////////")
#print (dicio_fornecedores)
