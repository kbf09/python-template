ARG PYTHON_VERSION=3.13
ARG UV_VERSION=0.5.14
ARG DEBIAN_VERSION=bookworm


# An example using multi-stage image builds to create a final image without uv.

# First, build the application in the `/app` directory.
# See `Dockerfile` for details.
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} AS builder
COPY --from=uv /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev
ADD . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev


# Then, use a final image without uv
FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION}
# It is important to use the image that matches the builder, as the path to the
# Python executable must be the same, e.g., using `python:3.11-slim-bookworm`
# will fail.

# 必要ならインストール
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#     # For OpenCV etc...
#     libgl1 libglib2.0-0 \
#     # To remove the image size, it is recommended refresh the package cache as follows
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# Copy the application from the builder
COPY --from=builder --chown=app:app /app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Run the application by default
CMD ["python", "/app/src/uv_docker_example"]