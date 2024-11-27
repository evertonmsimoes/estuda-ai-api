FROM python:3.12.7-slim
WORKDIR /

RUN pip install pipx && \
    pipx install poetry==1.8.4

ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY ./app .
COPY .main.py .
COPY  .pyproject.toml .
COPY  .env.local .


RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

WORKDIR /app

ENTRYPOINT ["poetry", "run", "python", "main.py"]