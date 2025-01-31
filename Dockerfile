FROM python:3.9-slim

WORKDIR /app
COPY main.py .

RUN pip install --no-cache-dir python-telegram-bot requests

CMD ["python", "main.py"]