#!/bin/bash
echo "Executing start_container.sh" >> /tmp/deployment.log
set -e
# Pull the Docker image from Docker Hub
docker pull tsmohitjain/task_manager
# Run the Docker image as a container
docker run -d -p 5000:5000 tsmohitjain/task_manager