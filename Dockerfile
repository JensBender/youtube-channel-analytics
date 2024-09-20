FROM apache/airflow:2.9.2-python3.9

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

RUN pip install --no-cache-dir \
    pandas \
    sqlalchemy \
    mysql-connector-python \
    google-api-python-client \
    gradio-client 
