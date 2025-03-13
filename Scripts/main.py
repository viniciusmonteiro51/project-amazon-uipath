import smtplib
import pandas as pd
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp-mail.outlook.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "devs.enviosautomatico@outlook.com"
SENHA = "3YGx@gJ'2&&DTm3"

EMAIL_ENVIO="dev.viniciusdanielmonteiro@gmail.com"

HTML_TEMPLATE_PATH = "template.html"

path = "destination.csv"
df = pd.read_csv(path)

regex_preco = r"R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}"
df['preco'] = df['preco'].astype(str).str.extract(f'({regex_preco})')

df = df.fillna("Não identificado")

try:
    with open(HTML_TEMPLATE_PATH, "r", encoding="utf-8") as file:
        html_template = file.read()
except Exception as e:
    print(f"❌ Erro ao carregar o template HTML: {e}")
    exit()

for index, row in df.iterrows():
    nome_jogo = row["nome_jogo"]
    preco = row["preco"]
    enviado_por = row["enviado_por"]
    vendido_por = row["vendido_por"]
    marca = row["marca"]
    material = row["material"]
    tema = row["tema"]
    genero = row["genero"]
    numero_jogadores = row["numero_jogadores"]
    descricao = row["descricao"]
    
    corpo_email = html_template.replace("{{nome_jogo}}", nome_jogo)
    corpo_email = corpo_email.replace("{{preco}}", preco)
    corpo_email = corpo_email.replace("{{enviado_por}}", enviado_por)
    corpo_email = corpo_email.replace("{{vendido_por}}", vendido_por)
    corpo_email = corpo_email.replace("{{marca}}", marca)
    corpo_email = corpo_email.replace("{{material}}", material)
    corpo_email = corpo_email.replace("{{tema}}", tema)
    corpo_email = corpo_email.replace("{{genero}}", genero)
    corpo_email = corpo_email.replace("{{numero_jogadores}}", numero_jogadores)
    corpo_email = corpo_email.replace("{{descricao}}", descricao)

    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_ENVIO
    msg["Subject"] = f"🔥 Oferta Especial: {nome_jogo} por {preco}!"
    msg.attach(MIMEText(corpo_email, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_REMETENTE, SENHA) 
        server.sendmail(EMAIL_REMETENTE, EMAIL_ENVIO, msg.as_string())
        server.quit()
        print(f"✅ E-mail enviado para {EMAIL_ENVIO} - {nome_jogo}")
    except Exception as e:
        print(f"❌ Erro ao enviar para {EMAIL_ENVIO}: {e}")

print("📩 Processamento concluído!")
