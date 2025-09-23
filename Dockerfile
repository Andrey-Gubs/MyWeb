    FROM python:3.9-slim
    WORKDIR /app
    RUN pip install -r flask
    COPY . .
    CMD ["python", "web.py"]
