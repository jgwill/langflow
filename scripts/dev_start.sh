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

# Install backend dependencies
make install_backend

# Ensure frontend dependencies are installed
if [ ! -d src/frontend/node_modules ]; then
    echo "Installing frontend dependencies"
    make install_frontend
fi

# Build frontend with explicit config path to avoid path issues
cd src/frontend
CI="" npx vite build --config vite.config.mts || { echo "Frontend build failed"; exit 1; }
cd -

# Run backend and frontend concurrently
make backend &
BACKEND_PID=$!
trap "kill $BACKEND_PID" EXIT

make frontend

