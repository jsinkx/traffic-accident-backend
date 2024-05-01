from models.models import models

def create_forecast_accident(model_id, data):
        # If the model is not found, the first model of all is taken
        model = (list(filter(lambda v: v['id'] == model_id, models)) or models)[0]
        
        return {
                'model_name': model['name'], 
                'model_ru_name': model['ru_name'], 
                'predicted_class': int(model['model'].predict(data)),
                'predicted_probabilities': model['model'].predict_proba(data).tolist()[0], # [probability_class_0, probability_class_1]
                'success': True 
        }        