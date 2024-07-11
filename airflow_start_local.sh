# Note: Execute this bash script in a WSL terminal when running Airflow locally on a Windows machine 

#!/bin/bash

# Set the AIRFLOW_PROJ_DIR environment variable to the current working directory
export AIRFLOW_PROJ_DIR=$(pwd)

# Set the AIRFLOW_UID environment variable
export AIRFLOW_UID=50000

# Build a custom Docker image from Dockerfile to include all required python libraries (e.g. pandas)
docker build -t custom-airflow:2.9.2 .

# Initialize the Airflow database and create the necessary directories and setup
docker compose up airflow-init

# Run the Airflow webserver and scheduler defined in docker-compose.yaml in detached mode
docker compose up -d 
