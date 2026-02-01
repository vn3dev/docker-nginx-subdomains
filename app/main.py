# server wen flask para exibir um html com o host e headers que o nginx injeta

from flask import Flask, request
import os

app = Flask(__name__)

DEFAULT_COLOR = os.getenv("COLOR", "#222") # tenta ler color, se não encontrar usa #222
DEFAULT_LABEL = os.getenv("CLIENT_LABEL", "cliente") # mesma coisa mas com o nome do cliente

@app.get("/") 
def home():
    host = request.headers.get("Host", "") # pega o header http do host, se n existir faz uma string vazia
    subdomain = host.split(".")[0] if "." in host else host # se o host tiver ".", ele divide a string e pega só a primeira parte antes do ponto

# pega label e color da requisição e se n tiver, usa default
    client_label = request.headers.get("X-Client-Label", DEFAULT_LABEL)
    color = request.headers.get("X-Color", DEFAULT_COLOR)

# estrutura html para exibir os dados
    return f"""
    <html>
      <body style="margin:0; font-family: Arial; background:{color}; color:white;">
        <div style="padding:48px;">
          <h1>Olá, {subdomain}!</h1>
          <p><b>CLIENT_LABEL</b>: {client_label}</p>
          <p><b>Host</b>: {host}</p>
        </div>
      </body>
    </html>
    """