#!/bin/bash
set -e

# Build and launch Langflow development servers
# Usage: ./scripts/dev_start.sh

# Ensure uv is available for dependency management
if ! command -v uv >/dev/null 2>&1; then
    echo "uv not found, installing via make setup_uv"
    make setup_uv
fi

# Copy env example if .env missing
if [ ! -f .env ]; then
    echo "Creating .env file"
    cp .env.example .env
fi

# Install dependencies and build frontend
make install_backend
make install_frontend
make build_frontend

# Run backend and frontend concurrently
make backend &
BACKEND_PID=$!
trap "kill $BACKEND_PID" EXIT

make frontend

