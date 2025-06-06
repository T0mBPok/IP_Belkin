FROM python:3.13-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src
COPY .env /app/.env

CMD ["python", "-m", "src.main"]
