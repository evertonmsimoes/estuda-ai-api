FROM python:3.12.7-slim

# Define o diretório de trabalho
WORKDIR /app

RUN pip install pipx && \
    pipx install poetry==1.8.4

ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false

# Copiar os arquivos necessários
COPY ./pyproject.toml .
COPY ./.env.local .
COPY ./main.py .
COPY ./app .


# Instalar dependências
RUN poetry install --no-interaction --no-ansi

# Expor a porta
EXPOSE 8000

# Comando para rodar o app
ENTRYPOINT ["poetry", "run", "python", "main.py"]
