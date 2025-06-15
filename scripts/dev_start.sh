#!/bin/bash
set -e

# Build Langflow and launch development servers
# Usage: ./scripts/dev_start.sh

make build

# Run backend and frontend concurrently
make backend &
BACKEND_PID=$!

make frontend

# When frontend exits (Ctrl+C), stop backend
kill $BACKEND_PID
