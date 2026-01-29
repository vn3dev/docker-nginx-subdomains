# sistema base -> debian, py3.12 e pip
FROM python:3.12-slim

# define o diretorio padrao, todo comando vai rodar como se estivesse aqui
WORKDIR /app
# copia o requirements.txt para dentro da imagem, como definimos diretorio atual podemos usar "."
COPY requirements.txt .
# instala tudo que esta dentro do requirements
# --no-cache-dir = nao guarda cache dos pacotes, reduz o tamanho da imagem e evita lixo
# -r = identifica requirements.txt como lista e nao como nome do pacote
RUN pip install --no-cache-dir -r requirements.txt

# copia o dummy app para o diretorio do workdir
COPY main.py .

# documentacao de portas usadas. Porta alta, sem privilegios
EXPOSE 8000
# roda sempre q o container inicia
# gunicorn eh o servidor WSGI
# -b de bind seguido do ip que ele vai escutar = escuta todas as interfaces dentro do container
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]