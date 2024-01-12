from models.models import models

def create_forecast_accident(model_id, data):
    # Если модель не найдена, берется первая модель из всех
    model = (list(filter(lambda v: v['id'] == model_id, models)) or models)[0]
    
    return {
            'model_name': model['name'], 
            'model_ru_name': model['ru_name'], 
            'forecasted_value': int(model['model'].predict(data)),
            'success': True 
    }        