FROM node:22-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json .
RUN npm install
COPY frontend/ .
RUN npm run build


FROM python:3.12-slim-bookworm AS backend-builder
COPY --from=ghcr.io/astral-sh/uv:0.6 /uv /uvx /bin/
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=backend/uv.lock,target=uv.lock \
    --mount=type=bind,source=backend/pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev


FROM python:3.12-slim-bookworm
WORKDIR /app
COPY --from=backend-builder /app/.venv /app/.venv
COPY ./backend .
COPY --from=frontend-builder /app/frontend/dist ./dist
ENV PATH="/app/.venv/bin:$PATH"

CMD [ "uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000" ]
