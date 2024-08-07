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
    try:
        # Ensure the request content type is JSON
        if request.is_json:
            # Parse the JSON data
            data = request.get_json()
            
            # Assume 'model' is your pre-trained model loaded elsewhere in your code
            prediction = model.predict([list(data.values())])
            
            return jsonify(prediction=prediction[0])
        else:
            return jsonify(error="Invalid content type, expecting JSON"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
