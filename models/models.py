import os 
import json
import joblib

def load_models():
        file = open(os.path.abspath('./models/models.json'), encoding="utf8")
        models = json.load(file)
        
        file.close() 

        for model in models:
                model_path = os.path.abspath(model['path'] + model['file']) # Getting the model path
                model['model'] = joblib.load(model_path) # Loading a model and saving it to the dictionary
                
                print(f'Loaded model { model["name"] }')
        
        return models
   
def info_model(model):
        clean_model = { **model }
        
        del clean_model['file']
        del clean_model['path']
        del clean_model['model']
        
        return clean_model


models = load_models()