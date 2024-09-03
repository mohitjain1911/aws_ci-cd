#!/bin/bash
set -e
# Pull the Docker image from Docker Hub
docker pull tsmohitjain/task_manager
# Run the Docker image as a container
docker run -d -p 5000:5000 abhishekf5/task_manager