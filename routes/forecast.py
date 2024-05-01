from flask import request, jsonify, Blueprint
from controllers.create_forecast import create_forecast_accident
from models.models import models, info_model

import pandas as pd

forecast_route_blueprint = Blueprint('forecast', __name__)

forecast_features = ['temperature', 'atmospheric_pressure', 'humidity', 'wind_speed', 'cloudiness', 'hour', 'season_autumn', 'season_spring', 'season_summer', 'season_winter']

@forecast_route_blueprint.route('/forecast', methods=['GET', 'POST'])
def forecast_route():
    if request.method == 'POST':
        data = request.get_json()
        
        try:
            model_id = int(data['model_id']) or 0
            df = pd.DataFrame([data['options']]) # Creating a pandas DataFrame from incoming data
            
            result = jsonify(create_forecast_accident(model_id, df[forecast_features])) # Creating a forecast of the model selected by id and the data selected by attributes
        except:
            result = jsonify({ 'success': False, 'message': 'Что-то пошло не так!'  }), 400
        return result
    else:
        clean_models = list(map(info_model, models))
        
        return jsonify(clean_models)