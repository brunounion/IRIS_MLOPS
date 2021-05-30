# iris_apy.py
# command to run it: gunicorn iris_api_gunicorn:app --bind 0.0.0.0:5000 --workers 4


from flask import Flask, request, jsonify
from src.inference import model_loader, model_predict
from src.config import MODELS_DIRECTORY
import numpy as np

app = Flask(__name__)

MODEL = None
DEVICE = "cpu"

features_names = ['sepal length (cm)',
                  'sepal width (cm)',
                  'petal length (cm)',
                  'petal width (cm)']

@app.route("/health_check", methods=["GET"])
def health_check():
    return 'ok'

@app.route("/predict", methods=["GET"])
def predict():
    X = list(map(float, request.args.to_dict().values()))
    loaded_model = model_loader( MODELS_DIRECTORY, 'plain_gaussian')
    classes_name_dict = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    prediction = model_predict(X, classes_name_dict = classes_name_dict, loaded_model = loaded_model)
    output = prediction
    output_X_values_list, class_number, class_name = output[0], output[1], output[2]

    output_dict = {'query' : dict(zip(features_names, output_X_values_list)), 'class_number' : class_number, 'class_name' : class_name}
    return jsonify(output_dict)

# if __name__ == "__main__":
    
#     #start the aplication
#     app.run(host = "0.0.0.0")
