FROM python:3.11-slim

RUN apt update && apt install --no-install-recommends -y git curl && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install mcpo uv

EXPOSE 8081

CMD ["uvx", "mcpo", "--port", "8081", "--server-type", "sse", "--", "http://0.0.0.0:8082/sse"]