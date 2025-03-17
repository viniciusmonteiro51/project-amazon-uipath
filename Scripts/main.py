import smtplib
import pandas as pd
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurações de e-mail
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "dev.enviostestes@gmail.com"
SENHA = "ynfh wgje uycv aqwa"

EMAIL_ENVIO = "dev.viniciusdanielmonteiro@gmail.com"
HTML_TEMPLATE_PATH = "template.html"

# path="Invoke Python Method: One or more errors occurred. (Erro ao invocar método Python)"

def sendMailGames(path):
    try:
        df = pd.read_csv(path)
    except Exception as e:
        return f"❌ Erro ao carregar o arquivo CSV: {e}"

    # Expressão regular para extrair preços corretamente
    regex_preco = r"R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}"
    df["preco"] = df["preco"].astype(str).str.extract(f"({regex_preco})")

    # Preenchendo valores nulos com "Não identificado"
    df = df.fillna("Não identificado")

    # Carregar o template HTML
    try:
        with open(HTML_TEMPLATE_PATH, "r", encoding="utf-8") as file:
            html_template = file.read()
    except Exception as e:
        return f"❌ Erro ao carregar o template HTML: {e}"

    # Iterar sobre cada linha do CSV
    for _, row in df.iterrows():
        nome_jogo = row.get("nome_jogo", "Não identificado")
        preco = row.get("preco", "Não identificado")
        enviado_por = row.get("enviado_por", "Não identificado")
        vendido_por = row.get("vendido_por", "Não identificado")
        idioma = row.get("idioma", "Não identificado")
        numero_modelo = row.get("numero_modelo", "Não identificado")
        fabricante = row.get("fabricante", "Não identificado")

        # Personalizar template do e-mail
        corpo_email = html_template
        corpo_email = corpo_email.replace("{{nome_jogo}}", nome_jogo)
        corpo_email = corpo_email.replace("{{preco}}", preco)
        corpo_email = corpo_email.replace("{{enviado_por}}", enviado_por)
        corpo_email = corpo_email.replace("{{vendido_por}}", vendido_por)
        corpo_email = corpo_email.replace("{{idioma}}", idioma)
        corpo_email = corpo_email.replace("{{numero_modelo}}", numero_modelo)
        corpo_email = corpo_email.replace("{{fabricante}}", fabricante)

        # Criar e configurar o e-mail
        msg = MIMEMultipart()
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = EMAIL_ENVIO
        msg["Subject"] = f"🔥 Oferta Especial: {nome_jogo} por {preco}!"
        msg.attach(MIMEText(corpo_email, "html"))

        # Enviar o e-mail
        try:
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA)
            server.sendmail(EMAIL_REMETENTE, EMAIL_ENVIO, msg.as_string())
            server.quit()
        except Exception as e:
            return f"❌ Erro ao enviar para {EMAIL_ENVIO}: {e}"

    return "📩 Processamento concluído com sucesso!"
