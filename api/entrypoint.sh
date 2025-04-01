#!/bin/bash
set -e # Exit on error

# Run migrations
echo "Running database migrations..."
uv run alembic upgrade head

# Start the application
echo "Starting application..."
exec uv run fastapi dev --host 0.0.0.0 --port 8000 