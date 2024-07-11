# Note: Execute this bash script in PuTTY when running Airflow on an AWS EC2 instance

#!/bin/bash

# Set the AIRFLOW_PROJ_DIR environment variable to the current working directory
export AIRFLOW_PROJ_DIR=$(pwd)

# Set the AIRFLOW_UID environment variable 
export AIRFLOW_UID=50000

# When running Airflow with Docker on EC2 t2.micro: Add 2GB of swap space (because 1GiB memory of t2.micro is not sufficient)
sudo fallocate -l 2G /swapfile  # Create a swap file 
sudo chmod 600 /swapfile  # Set correct permissions
sudo mkswap /swapfile  # Set up the swap area
sudo swapon /swapfile  # Enable the swap  

# Build a custom Docker image from Dockerfile to include all required python libraries (e.g. pandas)
docker build -t custom-airflow:2.9.2 .

# Initialize the Airflow database and create the necessary directories and setup
docker-compose up airflow-init

# Run Airflow webserver in detached mode
docker-compose up -d airflow-webserver

# Run Airflow scheduler in detached mode
docker-compose up -d airflow-scheduler
