import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random import randint
import gspread


class Amigo:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email


# Função para enviar e-mails
def enviar_email(destinatario, assunto, corpo):

    # Configurar o e-mail
    remetente = 'amigosecretoo.natal2023@gmail.com'
    mensagem = MIMEMultipart()
    mensagem['From'] = remetente
    mensagem['To'] = destinatario
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Adicionar o corpo do e-mail
    mensagem.attach(MIMEText(corpo, 'plain'))

    # Configurar o SendGrid (substitua com suas próprias informações)
    servidor_smtp = 'smtp.sendgrid.net'
    porta_smtp = 587
    usuario_smtp = 'apikey'
    senha_smtp = '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'

    # Iniciar a conexão com o servidor SMTP
    with smtplib.SMTP(host=servidor_smtp, port=porta_smtp) as servidor:
        servidor.starttls()

        # Autenticar com o SendGrid usando a chave da API
        servidor.login(usuario_smtp, senha_smtp)

        # Enviar e-mail
        servidor.send_message(mensagem)

# Configurando GSPREAD
gc = gspread.service_account(filename='Amigosecreto-404413-ea513199ac5d.json')

# Caminho da Planilha
planilha = gc.open('Amigo Secreto')

# Acessar a primeira guia da planilha
guia = planilha.sheet1

# Ler os dados da guia
dados = guia.get_all_records()

# Criar lista de participantes
participantes = []

# Agora, você tem os dados da planilha no formato de uma lista de dicionários
for linha in dados:
    nome = linha['Nome']
    email = linha['Email']
    amigo = Amigo(nome, email)
    participantes.append(amigo)

sorteio = {}  # Um dicionário para armazenar o resultado do sorteio

# Realizar o sorteio dos amigos e armazenar o resultado no dicionário 'sorteio'
for participante in participantes:
    try:
        index = randint(0, len(participantes) - 1)

        while participante.nome == participantes[index].nome:
            index = randint(0, len(participantes) - 1)

        amigo_sorteado = participantes[index]
        sorteio[participante] = amigo_sorteado

        # Remover o amigo sorteado da lista para evitar duplicatas
        participantes.pop(index)


        # Enviar e-mail com o resultado personalizado
        destinatario = participante.email  # Substitua pelo e-mail real do participante
        assunto = 'Resultado do Amigo Secreto'
        corpo = f'Olá {participante.nome}, você tirou {amigo_sorteado.nome} no Amigo Secreto!'

        enviar_email(destinatario, assunto, corpo)

    except:
        print(f"Erro ao enviar email para: {participante.nome}")
