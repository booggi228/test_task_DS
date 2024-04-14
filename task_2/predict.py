import pandas as pd
import numpy as np
import joblib
# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    # Load the inference data
    inference_data = pd.read_csv('data/hidden_test.csv')

    # Load the scaler
    scaler = joblib.load('artifacts/scaler.pkl')

    # Load the model
    model = joblib.load('artifacts/model.pkl')

    # Drop correlated feature
    inference_data = inference_data.drop('6', axis = 1)

    # Transform the inference data using the loaded scaler
    inference_data_scaled = scaler.transform(inference_data)

    # Make predictions
    predictions = model.predict(inference_data_scaled)

    # Save the predictions to a file
    output_df = pd.DataFrame({'Prediction': predictions})
    output_df.to_csv('output/predictions.csv', index=False) 