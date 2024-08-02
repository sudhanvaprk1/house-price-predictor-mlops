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
    
    # Drop the first index column
    raw_data = raw_data.iloc[:, 1:]
    
    # Remove Unnamed columns
    raw_data = raw_data.loc[:, ~raw_data.columns.str.contains('^Unnamed')]

    # Dropping null values 
    processed_data = raw_data.dropna()

    # Encode categorical variables
    processed_data = pd.get_dummies(processed_data, drop_first=True)

    # Saving processed data
    processed_data.to_csv(os.getcwd() + processed_data_path, index=False)
    print("Data has been processed successfully")

        
process_raw_data()
