FROM node:20 AS base

WORKDIR /frontend
RUN npm install create-next-app -g

RUN npx create-next-app mysite --ts --tailwind --eslint --app --src-dir --import-alias @/*

WORKDIR /frontend/mysite