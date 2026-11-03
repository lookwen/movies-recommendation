FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY data/ ./data/
COPY frontend/ ./frontend/

EXPOSE 5000

CMD ["python", "-m", "frontend.app"]

