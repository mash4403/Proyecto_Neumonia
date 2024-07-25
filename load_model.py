# Propósito: Contiene la función para cargar el modelo entrenado desde un archivo .h5.

from keras.models import load_model

def load_trained_model():
    model_path = '/Users/miguelangel/Downloads/keras_model.h5'
    model_cnn = load_model(model_path)
    return model_cnn
