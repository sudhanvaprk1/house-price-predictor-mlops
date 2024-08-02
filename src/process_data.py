import pandas as pd
import os

def process_raw_data(raw_data_path='/datasets/raw/housing.csv',
                     processed_data_path="/datasets/processed/housing.csv"):
    """
    Reads the raw data, applies preprocessing techniques and stores processed data
    """ 
    # Making folders
    os.makedirs(f"{os.getcwd()}/datasets/processed/", exist_ok=True)

    # Reading raw data
    raw_data = pd.read_csv(os.getcwd() + raw_data_path)

    # Dropping null values 
    processed_data = raw_data.dropna()

    # Encode categorical variables
    processed_data = pd.get_dummies(processed_data, drop_first=True)

    # Saving processed data
    processed_data.to_csv(os.getcwd() + processed_data_path)
    print("Data has been processed successfully")

        
            
