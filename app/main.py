from flask import Flask, request
import os

app = Flask(__name__)

DEFAULT_COLOR = os.getenv("COLOR", "#222")
DEFAULT_LABEL = os.getenv("CLIENT_LABEL", "cliente")

@app.get("/")
def home():
    host = request.headers.get("Host", "")
    subdomain = host.split(".")[0] if "." in host else host

    client_label = request.headers.get("X-Client-Label", DEFAULT_LABEL)
    color = request.headers.get("X-Color", DEFAULT_COLOR)

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