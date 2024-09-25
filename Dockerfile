FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set the working directory
WORKDIR /app

# Copy the src directory
COPY pyproject.toml .
COPY uv.lock .
COPY src/ .
COPY .env .

# Install dependencies
RUN uv sync

# Command to run the Streamlit app
CMD ["uv", "run", "streamlit", "run", "app.py"]
