import gspread
from random import randint


class Amigo:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

amigos = []  # Uma lista para armazenar objetos do tipo Amigo
amigos_aux = []  # Uma lista auxiliar para evitar que um amigo sorteie a si mesmo


# Configurando GSPREAD
gc = gspread.service_account(filename='amigosecreto-404413-f2c5ef70e4cb.json') # Fornecer o caminho do arquivo da chave .json

# Caminho da Planilha
planilha = gc.open('Amigo Secreto')
# Abrir a nova planilha no Google Sheets
nova_planilha = gc.create('Resultados do Sorteio Amigo Secreto')
# Adicionar os cabeçalhos
cabecalhos = ["Participante", "Sorteado"]
nova_planilha.sheet1.append_row(cabecalhos)



# Acessar a primeira guida da planilha
guia = planilha.sheet1

# Ler os dados da guia

dados = guia.get_all_records()

# Agora, você tem os dados da planilha no formato de uma lista de dicionários
for linha in dados:
    nome = linha['Nome']
    whatsapp = str(linha.get('Whatsapp', ''))
    telefone = '55' + whatsapp
    amigo = Amigo(nome, telefone)
    amigos.append(amigo)
    amigos_aux.append(amigo)


sorteio = {}  # Um dicionário para armazenar o resultado do sorteio

# Realizar o sorteio dos amigos e armazenar o resultado no dicionário 'sorteio'
for amigo in amigos:
    index = randint(0, len(amigos_aux) - 1)

    while amigo.nome == amigos_aux[index].nome:
        index = randint(0, len(amigos_aux) - 1)

    sorteio[amigo] = amigos_aux[index]  # Armazena o amigo sorteado no dicionário
    print("{} sorteou {}".format(amigo.nome, amigos_aux[index].nome)) # Utilizado apenas no momento do teste para ver se o sistema de sorteio funciona.
    del amigos_aux[index]  # Remove o amigo sorteado da lista auxiliar

# Escrever os resultados na planilha
for amigo, sorteado in sorteio.items():
    linha = [amigo.nome, sorteado.nome]
    nova_planilha.sheet1.append_row(linha)
