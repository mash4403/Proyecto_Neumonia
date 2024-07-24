
# Propósito: Integra las funciones de lectura de imágenes, preprocesamiento, predicción y visualización.
#Contenido:predict(array): Preprocesa la imagen, carga el modelo y genera predicciones y mapas de calor.
# Llama a las funciones definidas en otros módulos (read_img.py, load_model.py, grad_cam.py).

import numpy as np
from load_model import load_trained_model
from preprocess_img import preprocess
from grad_cam import grad_cam

def predict(array):
    model = load_trained_model()
    batch_array_img = preprocess(array)
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    elif prediction == 1:
        label = "normal"
    elif prediction == 2:
        label = "viral"
    heatmap = grad_cam(array, model)
    return label, proba, heatmap
