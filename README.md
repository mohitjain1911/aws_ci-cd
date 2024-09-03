# Task Manager - Flask on AWS with CI/CD

This repository contains the code for a Task Manager application built using Flask, Docker, and deployed on AWS EC2 using a CI/CD pipeline. The CI/CD pipeline leverages AWS CodeCommit, CodeBuild, and CodeDeploy.

## Features
- **Flask Application**: A simple task manager built with Flask.
- **Docker**: Containerized using Docker for easy deployment.
- **AWS CI/CD**: Automated deployment using AWS services like CodeCommit, CodeBuild, and CodeDeploy.

## Prerequisites
- AWS Account
- Docker installed
- Python 3.x installed
- AWS CLI configured

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/mohitjain1911/aws_ci-cd.git
    cd aws_ci-cd
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Build Docker image**:
    ```bash
    docker build -t task-manager .
    ```

4. **Run Docker container**:
    ```bash
    docker run -d -p 5000:5000 task-manager
    ```

5. **Deploy to AWS using CI/CD**:
    - Push your code to AWS CodeCommit.
    - CodeBuild will build the Docker image and push it to Amazon ECR.
    - CodeDeploy will deploy the application to an EC2 instance.

## Files

- `app.py`: Flask application code.
- `Dockerfile`: Docker configuration.
- `appspec.yml`: Configuration for AWS CodeDeploy.
- `buildspec.yml`: Configuration for AWS CodeBuild.
- `start_container.sh`: Script to start the Docker container.
- `stop_container.sh`: Script to stop the Docker container.

## License

This project is licensed under the MIT License.
