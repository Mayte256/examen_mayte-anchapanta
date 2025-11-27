# Imagen base ligera de Python
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto interno que escuchará Flask
EXPOSE 1003

CMD ["python", "app.py"]
