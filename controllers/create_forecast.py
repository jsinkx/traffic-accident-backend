import os
import joblib

MODEL_PATH = os.path.join('./ml-models', 'random_forest_model.pkl')
model = joblib.load(MODEL_PATH)

def create_forecast_accident(data): 
    return { 'forecasted_values': model.predict(data).tolist() }
