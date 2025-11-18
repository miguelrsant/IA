FROM python:3.12-slim

WORKDIR /app

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    libpq-dev \
    && apt-get clean

# Instala o PDM
RUN pip install --no-cache-dir pdm

# Copia apenas os arquivos de dependências primeiro (cache)
COPY pyproject.toml pdm.lock /app/

# Instala dependências de produção no ambiente isolado
RUN pdm install --prod --no-editable

# Copia o restante do código
COPY . /app

# Torna entrypoint executável
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Porta do Flask
EXPOSE 8000

ENV FLASK_APP=main.py

ENTRYPOINT ["/entrypoint.sh"]
