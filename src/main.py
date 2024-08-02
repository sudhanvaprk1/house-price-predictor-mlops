from flask import Flask, request, jsonify
from flask_cors import CORS
import mlflow
import numpy as np
from get_data import generate_data
from train_model import train_model
from process_data import process_raw_data
import os

app = Flask(__name__)
CORS(app)

# Generating train data
generate_data()

# Processing raw data
process_raw_data()

# Checking if the model is already present, if not, training new bagging model
experiment_name = "house-price-predictor"
model_name = "RandomForestHousePricePredictor"
if not os.path.exists(os.getcwd() + '/mlruns/'):
    # Train the model by tuning hyperparameters
    train_model(experiment_name = experiment_name,
                model_name = model_name)
    
# Get the latest version of the registered model
client = mlflow.tracking.MlflowClient()
latest_version_info = client.get_latest_versions(name=model_name, 
                                                 stages=["None", "Staging", "Production"])[-1]

# Load the latest version of the model
model_uri = f"models:/{model_name}/{latest_version_info.version}"
model = mlflow.pyfunc.load_model(model_uri)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data])
    return jsonify(prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
