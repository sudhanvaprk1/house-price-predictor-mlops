from sklearn.model_selection import train_test_split
import os 
import pandas as pd
from sklearn.preprocessing import StandardScaler

def get_processed_data(processed_data_path="/datasets/processed/housing.csv"):
    """
    Reads processed data
    """
    data = pd.read_csv(os.getcwd() + processed_data_path)
    return data

def split_data(data, target_var='median_house_value', test_size=0.2):
    """
    Takes a dataframe and splits it into train and test
    """
    # Splitting the data into X and y
    X = data.drop(target_var, axis=1)
    y = data[target_var]

    # Splitting the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=test_size, 
                                                        random_state=42)
    
    return X_train, X_test, y_train, y_test

def engineer_features():
    """
    Reads processed data, performs feature engg, splits the data into train and test
    """
    # Fetch processed data 
    data = get_processed_data()

    # Splitting the data
    X_train, X_test, y_train, y_test = split_data(data)

    # Scaling numerical values
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test



