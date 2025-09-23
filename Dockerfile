    FROM python:3.9-slim
    WORKDIR /app
    COPY . /app
    RUN pip install --no-cache-dir flask 
    ENTRYPOINT ["python3", "./Web.py"]
