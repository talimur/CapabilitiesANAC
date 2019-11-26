import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd

# site a ser iterado https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=0000000001 to 0000001500


i = 1

#roda atraves dos numeros de fornecedor
for i in range(i,2):
  pagina = requests.get(("https://sistemas.anac.gov.br/certificacao/AvGeral/AIR145BasesDetail.asp?B145Codi=000000"+ str('%04d'%i)))

#transforma página em objeto
soup = BeautifulSoup(pagina.text, 'lxml')
#text = soup.get_text()

#separa as tabelas do arquivo
tables = soup.findAll('table', width="710")


#pega apenas os campos da tabela que tem atributos de texto
tabela_basica = tables[3].findAll('font')


#limpa as tags da tabela
for tag in tabela_basica: 
  tag.attrs = None


print (len(tabela_basica)) #teste para verificar a quantidade de itens na tabela

print ("///////////////////////////////") #divisor

#imprime a posição e cada item da posição na tabela
nova_tabela = []
for i in tabela_basica:
  texto = [i.text]
  nova_tabela.append((i.get_text("'", strip=True)))

print (nova_tabela)
  
dicio_fornecedores = { i : nova_tabela[i] for i in range(0, len(nova_tabela) ) }
#print (tabela_basica)
print ("///////////////////////////////")
print (dicio_fornecedores)
