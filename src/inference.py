#inference.py

import pickle 
import numpy as np

MODELS_DIRECTORY = 'models/'

def model_loader(models_folder, models_name):
    return pickle.load(open(models_folder + models_name + '.pkl', 'rb'))
    
classes_name_dict = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

def model_predict(X, classes_name_dict, loaded_model ):
    X = np.array([X])
    target_value = loaded_model.predict(X)[0].tolist()
    predicted_class = classes_name_dict[target_value]
    return [X[0].tolist(), target_value, predicted_class]