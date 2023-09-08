FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1
ENV HTTP_PORT=8085

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y iputils-ping
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8085

CMD ["python", "main.py"]
