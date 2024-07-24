import numpy as np
from preprocess_img import preprocess
from load_model import load_model
from grad_cam import grad_cam

def predict(array):
    # Preprocesar la imagen
    batch_array_img = preprocess(array)
    # Cargar el modelo
    model = load_model()
    # Predecir la clase y la probabilidad
    prediction = np.argmax(model.predict(batch_array_img))
    proba = np.max(model.predict(batch_array_img)) * 100
    label = ""
    if prediction == 0:
        label = "bacteriana"
    elif prediction == 1:
        label = "normal"
    elif prediction == 2:
        label = "viral"
    # Generar el mapa de calor
    heatmap = grad_cam(array, model)
    return label, proba, heatmap
