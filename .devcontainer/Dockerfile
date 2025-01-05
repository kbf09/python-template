ARG PYTHON_VERSION=3.13
ARG UV_VERSION=0.5.13
ARG DEBIAN_VERSION=bookworm

FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} AS builder
COPY --from=uv /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1

# 必要ならインストール
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
