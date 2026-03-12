FROM node:22-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package*.json .
RUN npm install
COPY frontend/ .
RUN npm run build


FROM python:3.11-slim AS server
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY ./backend .
COPY --from=frontend-builder /app/frontend/dist ./dist
CMD [ "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000" ]
