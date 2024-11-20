FROM python:3.12.7
WORKDIR /

RUN apt-get update && apt-get install -y git && \
    pip install pipx && \
    git clone https://github.com/python-poetry/poetry.git && \
    cd poetry && \
    git checkout 4ea63a293b0b938e85eabd61f329abc01a89ed9a && \
    pipx install . \
    rm -rf poetry && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/root/.local/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY . .

COPY .env .

RUN poetry install --no-interaction --no-ansi

EXPOSE 8000

ENTRYPOINT ["poetry", "run", "python", "main.py"]