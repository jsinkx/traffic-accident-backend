from flask import Flask
from flask_cors import CORS

from shared.config import SERVER_HOST, SERVER_PORT, IS_PROD

def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    from routes.forecast import forecast_route_blueprint

    app.register_blueprint(forecast_route_blueprint)
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=(not IS_PROD), threaded=True)
