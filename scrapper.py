import requests
import lxml
from bs4 import BeautifulSoup

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

    #cria listas para iteração
      nova_lista = []
      new_list = []
      
    #move os conteudos para nova lista sem as tags
    for i in tabela_basica:
      nova_lista.append((i.get_text(",", strip=True)))

    #remove '\xa0' e divide a string
    for i in  nova_lista:
      new_list.extend(i.split('\xa0'))

    #troca ',' por '-'
    for i in range(len(new_list)):
      new_list[i] = new_list[i].replace(',',' -')

    #adiciona a lista na posição do dicionário de acordo com o número do endereço do fornecedor (-1)
    file.write(str(new_list).replace("'","").replace("[","").replace(";","").replace(":","")+ '\n')
    
