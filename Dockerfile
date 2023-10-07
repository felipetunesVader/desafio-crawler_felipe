FROM python:3

# Atualiza o sistema e instala as ferramentas necessárias
RUN apt-get update && apt-get install -y wget gnupg unzip

# Adiciona a chave de assinatura do Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adiciona o repositório do Google Chrome
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

# Instala o Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Baixa e instala a versão do ChromeDriver que é compatível com a versão do Chrome
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.149/linux64/chromedriver-linux64.zip -O chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver


WORKDIR /app

COPY . .

ENV TZ="America/Sao_Paulo"

RUN pip install --no-cache-dir selenium psycopg2-binary pandas

CMD ["python", "./app.py"]
