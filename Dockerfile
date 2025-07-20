FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && \
    apt-get install -y --no-install-recommends postgresql-client && \
    rm -rf /var/lib/apt/lists/*

WORKDIR .

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

COPY src ./src
COPY shared ./shared
# COPY alembic.ini ./
# COPY migration ./migration

ENV PYTHONPATH=/shared:/src

RUN echo '#!/bin/sh' > /entrypoint.sh && \
    # echo 'set -e' >> /entrypoint.sh && \
    # echo '' >> /entrypoint.sh && \
    # echo 'echo "Ожидание доступности PostgreSQL..."' >> /entrypoint.sh && \
    # echo 'until pg_isready -h pg -p ${PG_PORT} -q; do' >> /entrypoint.sh && \
    # echo '  sleep 1' >> /entrypoint.sh && \
    # echo 'done' >> /entrypoint.sh && \
    # echo '' >> /entrypoint.sh && \
    # echo 'echo "Запуск миграций Alembic..."' >> /entrypoint.sh && \
    # echo 'uv run alembic upgrade head' >> /entrypoint.sh && \
    # echo '' >> /entrypoint.sh && \
    echo 'echo "Запуск приложения..."' >> /entrypoint.sh && \
    echo 'exec uv run uvicorn src.main:app --host 0.0.0.0 --port 8000' >> /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8000

CMD ["/entrypoint.sh"]