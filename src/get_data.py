import pandas as pd
import os

def generate_data(file_path="/datasets/raw/housing.csv"):
    """
    Checks if the raw data is present at the dedicated path, else fetches the csv file via github
    URL and stores the data under raw
    """
    # Checking if the file path exists
    if not os.path.exists(file_path):
        # Making folders
        os.makedirs(f"{os.getcwd()}/datasets/raw/", exist_ok=True)

        # Load the dataset
        url = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv'
        data = pd.read_csv(url)
        data.to_csv(os.getcwd() + file_path)
        print('Training Data has been successfully fetched')
    else:
        print("Training Data already exists, skipping the data fetch process.")

