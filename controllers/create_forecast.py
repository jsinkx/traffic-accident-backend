# import lime
# import lime.lime_tabular
from models.models import models

def create_forecast_accident(model_id, data):
        # Если модель не найдена, берется первая модель из всех
        model = (list(filter(lambda v: v['id'] == model_id, models)) or models)[0]

        # todo: добавить локальную интерпретацию случая

        # explainer = lime.lime_tabular.LimeTabularExplainer(data.values, feature_names=data.columns.values.tolist(), class_names=['accident', 'no accident'], mode='classification')
        # exp = explainer.explain_instance(data.values[0], model['model'].predict_proba, num_features=len(data.columns))
    
        # exp.save_to_file('./cache/lime.html')
        
        return {
                'model_name': model['name'], 
                'model_ru_name': model['ru_name'], 
                'predicted_class': int(model['model'].predict(data)),
                'predicted_probabilities': model['model'].predict_proba(data).tolist()[0], # [вероятность_класс_0, вероятность_класс_1]
                'success': True 
        }        