# This file is specific to HuggingFace spaces, since it relies on having a user prior to copying or
# downloading files to avoid permission issues.

# Build the application in the `/app` directory.
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim AS builder
# Enable bytecode compilation.
ENV UV_COMPILE_BYTECODE=1
# Copy from the cache instead of linking since it's a mounted volume.
ENV UV_LINK_MODE=copy
# Use the system interpreter across both images.
ENV UV_PYTHON_DOWNLOADS=0

# Create a user to copy and download files. Hugging Face requirement.
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH
# Set up '/app' as working directory.
WORKDIR $HOME/app

# Change env var UV_CACHE_DIR
ENV UV_CACHE_DIR=$HOME/.cache/uv
# Install the project's dependencies using the lockfile and settings.
COPY --chown=user uv.lock pyproject.toml $HOME/app/
RUN --mount=type=cache,target=$UV_CACHE_DIR \
    uv sync --frozen --no-install-project --no-dev
# Add the rest of the source code and install it.
# Installing separately from its dependencies allows optimal layer caching.
COPY --chown=user datasets/english_models.csv $HOME/app/datasets/english_models.csv
COPY --chown=user main.py $HOME/app
RUN --mount=type=cache,target=$UV_CACHE_DIR \
  uv sync --frozen --no-dev

# Final image with uv support to run the main script.
FROM python:3.11-slim-bookworm

# Create a user to copy and download files. Hugging Face requirement.
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH
# Set up '/app' as working directory.
WORKDIR $HOME/app

# Try and run pip command after setting the user with `USER user` to avoid permission issues with Python
RUN pip install --no-cache-dir --upgrade pip

# Copy the application from the builder.
COPY --from=builder --chown=user $HOME/app $HOME/app
# Install UV
RUN pip install uv
# Place executables in the path environment variable.
ENV PATH="$HOME/app/.venv/bin:$PATH"

# Set up server and port 7860, required by gradio.
EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Command to run the app with UV.
ENTRYPOINT ["uv", "run", "main.py"]