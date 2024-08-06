# MLOps Assignment M3 - House Price Predictor Flask Application

This repository contains a Flask application that tunes a Random Forest Regressor using Optuna, logs the model using MLflow, and uses this model to predict house prices. The application runs in a Docker container.

## Repository Structure

```
├── .github/workflows
|   ├── docker-image.yml       # CI/CD Workflow 
├── env
│   ├── requirements.txt       # Python dependencies
│   └── environment.yml        # Conda environment configuration
├── src
│   ├── main.py                # Flask application code
│   └── ml_workflow.py         # Sample ML workflow code
├── Dockerfile                 # Dockerfile for creating Docker image
└── README.md                  # Project overview and setup instructions
```


## Description

- **env**: Contains files for setting up the development environment.
  - `requirements.txt`: Lists the Python dependencies required for the project.
  - `environment.yml`: Defines the Conda environment with necessary packages.

- **src**: Contains the source code for the machine learning workflow and the Flask application.
  - `main.py`: The main entry point for the Flask application.
  - `ml_workflow.py`: Contains code for training the Random Forest Regressor using Optuna, logging the model with MLflow, and other related tasks.

- **Dockerfile**: Defines the Docker image configuration to run the Flask application.

## Features

- **Model Tuning**: Uses Optuna to perform hyperparameter tuning on a Random Forest Regressor.
- **Model Logging**: Logs the tuned model using MLflow for tracking and reproducibility.
- **Prediction**: Uses the trained model to predict house prices based on input features.

## Setup Instructions

### 1. Create Environment

You can set up the environment using either `requirements.txt` or `environment.yml`.

#### Using Conda

```
conda env create -f env/environment.yml
conda activate your_env_name
```

#### Using Pip

```
pip install -r env/requirements.txt
```

### 2. Run the Application

#### Locally

```
python src/main.py
```

#### Using Docker

### 1. Build the Docker Image

```
docker build -t hpp-mlops-app .
```

### 2. Run the Docker Container

```
docker run -p 5000:5000 flask-ml-app
```

This will start the Flask application and make it accessible at http://localhost:5000.

#### Using GitHubAction workflow to trigger the CI/CD pipeline 

```
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

on: specifies the events that trigger the workflow.

push: indicates that the workflow will be triggered on push events to the main branch. This means whenever code is pushed to the main branch, this workflow will run.

pull_request: indicates that the workflow will also be triggered when a pull request is created or updated against the main branch. This helps ensure that code changes are validated in pull requests before being merged.

```
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Build the Docker image
      run: docker build . -t 399622/house-price-predictor:latest --file Dockerfile --tag my-image-name:$(date +%s)
  
    - name: Publish Docker Image
      run: |
        docker login -u 399622 -p ${{ secrets.DOCKER_HUB_TOKEN}}
        docker push 399622/house-price-predictor:latest
```
jobs:
Defines the jobs that make up the workflow. Each job runs in its own virtual environment.
build:
The name of the job. In this case, it's called build.
runs-on: ubuntu-latest
Specifies the type of runner (virtual machine) to run the job on. ubuntu-latest uses the latest version of Ubuntu available in GitHub-hosted runners.
steps:
A sequence of steps to be executed as part of the job.
- uses: actions/checkout@v4
This step uses the actions/checkout action, which checks out your repository so that subsequent steps can access its contents. @v4 specifies the version of this action.

- name: Build the Docker image
Provides a name for the step. This step builds a Docker image.

```
run: docker build . -t 399622/house-price-predictor:latest --file Dockerfile --tag my-image-name:$(date +%s)

```
docker build . builds a Docker image from the Dockerfile located in the root directory of the repository.
-t 399622/house-price-predictor:latest tags the built image with the name 399622/house-price-predictor and the tag latest.
--file Dockerfile specifies the Dockerfile to use for the build (the default is Dockerfile, so this option is optional if the Dockerfile is named Dockerfile).
--tag my-image-name:$(date +%s) additionally tags the image with a unique tag based on the current timestamp (to avoid conflicts with other images).

- name: Publish Docker Image
Provides a name for the step. This step pushes the Docker image to a Docker registry (in this case, Docker Hub).

```
run: |
  docker login -u 399622 -p ${{ secrets.DOCKER_HUB_TOKEN}}
  docker push 399622/house-price-predictor:latest
```

docker login -u 399622 -p ${{ secrets.DOCKER_HUB_TOKEN}} logs in to Docker Hub using a username (399622) and a password (retrieved from GitHub Secrets using ${{ secrets.DOCKER_HUB_TOKEN }}).
docker push 399622/house-price-predictor:latest pushes the Docker image tagged as latest to the Docker Hub repository 399622/house-price-predictor.

## Usage

Once the Flask application is running, you can send requests to the endpoints to get house price predictions. Make sure to refer to the API documentation or the main.py file for the available endpoints and their usage.
