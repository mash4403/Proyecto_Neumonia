import tensorflow as tf
from tensorflow.keras.models import load_model

def load_trained_model():
    model_path = '/Users/miguelangel/Documents/inteligencia artificial/REPOSITORIOS/Proyecto_Neumonia/conv_MLP_84.h5'
    model_cnn = load_model(model_path, compile=False)
    return model_cnn
