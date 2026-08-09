FROM python:3.14-slim AS builder

WORKDIR /src

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

COPY pyproject.toml pyproject.toml

COPY uv.lock uv.lock

RUN uv sync --python /usr/local/bin/python3

FROM python:3.14-slim

WORKDIR /src

COPY --from=builder /src/.venv /src/.venv

COPY src ./src

EXPOSE 8000

CMD ["/src/.venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]