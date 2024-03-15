FROM python:3.12.2

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend
COPY . .
RUN apt update && apt upgrade -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /backend/djangobackend