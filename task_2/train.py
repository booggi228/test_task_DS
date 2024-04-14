import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import joblib
# Ignore warnings
import warnings
warnings.filterwarnings("ignore")


if __name__ == '__main__':
    # Load the training data
    train_data = pd.read_csv('data/train.csv')

    # Split the data into features and target variable, drop correlated column - '6'
    X = train_data.drop(columns=['target', '6'])
    y = train_data['target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_test)

    # Initialize Lasso model
    lasso = Lasso()

    # Train model
    lasso.fit(X_train, y_train)

    # Evaluate model on train and test data
    train_predictions = lasso.predict(X_train_scaled)
    train_rmse = mean_squared_error(y_train, train_predictions, squared=False)
    print("Train RMSE:", np.round(train_rmse, 2))

    test_predictions = lasso.predict(X_val_scaled)
    test_rmse = mean_squared_error(y_test, test_predictions, squared=False)
    print("Test RMSE:", np.round(test_rmse, 2))

    # Save Lasso model
    joblib.dump(lasso, 'artifacts/model.pkl')
    joblib.dump(scaler, 'artifacts/scaler.pkl')
