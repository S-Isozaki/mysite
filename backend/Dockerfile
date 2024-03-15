FROM python:3.12.2-alpine3.19 AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /backend
COPY ./requirements.txt .
RUN pip install -r requirements.txt