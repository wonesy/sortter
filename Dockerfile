FROM python:3.10

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/

RUN ls

RUN poetry config virtualenvs.create false && poetry install

COPY . /app

WORKDIR /app/sortter

ENTRYPOINT [ "uvicorn", "main:app", "--port", "8088", "--host", "0.0.0.0"]