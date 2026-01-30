from flask import Flask, request
import os

app = Flask(__name__)

COLOR = os.getenv("COLOR", "#222")
CLIENT_LABEL = os.getenv("CLIENT_LABEL", "cliente")

@app.get("/")
def home():
    host = request.headers.get("Host", "")
    subdomain = host.split(".")[0] if "." in host else host

    return f"""
    <html>
      <body style="margin:0; font-family: Arial; background:{COLOR}; color:white;">
        <div style="padding:48px;">
          <h1>Olá, {subdomain}!</h1>
          <p><b>CLIENT_LABEL</b>: {CLIENT_LABEL}</p>
          <p><b>Host</b>: {host}</p>
        </div>
      </body>
    </html>
    """