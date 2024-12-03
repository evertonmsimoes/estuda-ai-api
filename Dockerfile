FROM python:3.12.7-slim

# Define o diretório de trabalho
WORKDIR /

 RUN apt-get update && apt-get install -y git && \
     pip install pipx && \
     git clone https://github.com/python-poetry/poetry.git && \
     cd poetry && \
     pipx install .

ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false

# Copiar os arquivos necessários
COPY ./pyproject.toml .
COPY ./.env.local .
COPY ./main.py .
COPY ./app .


# Instalar dependências
RUN poetry install --no-interaction --no-ansi

WORKDIR /app

# Expor a porta
EXPOSE 8000

# Comando para rodar o app
ENTRYPOINT ["poetry", "run", "python", "main.py"]
