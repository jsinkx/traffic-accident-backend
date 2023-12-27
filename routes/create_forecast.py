from flask import request, jsonify, Blueprint

import pandas as pd

from controllers.create_forecast import create_forecast_accident

forecast_route_blueprint = Blueprint('forecast', __name__)

@forecast_route_blueprint.route('/forecast', methods=['POST'])
def forecast_route():
    data = request.get_json()
    
    try:
        df = pd.DataFrame(data)
        result = create_forecast_accident(df)
    except:
        result = { 'success': False }
    return jsonify(result)