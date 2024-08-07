# MLOps Assignment M3 - House Price Predictor Flask Application

This repository contains a Flask application that tunes a Random Forest Regressor using Optuna, logs the model using MLflow, and uses this model to predict house prices. The application runs in a Docker container.

## Repository Structure

```
├── .github
│ └── workflows
│ └── ci-cd.yml # GitHub Actions workflow for CI/CD pipeline
├── env
│ ├── requirements.txt # Python dependencies
│ └── environment.yml # Conda environment configuration
├── src
│ ├── get_data.py # Script to fetch and load data
│ ├── feature_engineering.py # Script for feature engineering
│ ├── process_data.py # Script for processing data
│ ├── train_model.py # Script to train the model
│ ├── hyperparameter_tuning.py # Script for hyperparameter tuning using Optuna
│ └── main.py # Flask application code
├── Dockerfile # Dockerfile for creating Docker image
└── README.md # Project overview and setup instructions
```


## Description

- **.github/workflows**: Contains the GitHub Actions workflows.
  - `ci-cd.yml`: Defines the CI/CD pipeline, including stages for linting, formatting, and deploying the Docker image.

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

## Usage

Once the Flask application is running, you can send requests to the endpoints to get house price predictions. Make sure to refer to the API documentation or the main.py file for the available endpoints and their usage.
