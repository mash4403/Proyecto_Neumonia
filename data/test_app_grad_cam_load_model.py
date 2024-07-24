import pytest
import numpy as np
from integrator import predict
from read_img import read_dicom_file, read_jpg_file
from preprocess_img import preprocess
from grad_cam import grad_cam
from load_model import load_trained_model

def test_preprocess():
    array = np.random.randint(0, 255, (600, 600, 3), dtype=np.uint8)
    result = preprocess(array)
    assert result.shape == (1, 512, 512, 1), "El preprocesamiento no devuelve el formato correcto"

def test_predict():
    array = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    label, proba, heatmap = predict(array)
    assert label in ["bacteriana", "normal", "viral"], "La predicción no devuelve una etiqueta válida"
    assert 0 <= proba <= 100, "La probabilidad no está en el rango esperado"

def test_read_dicom_file():
    path = "data/sample.dcm"  # Asegúrate de que esta ruta sea correcta para tu archivo DICOM de prueba
    img_RGB, img2show = read_dicom_file(path)
    assert img_RGB.shape == (512, 512, 3), "La imagen leída no tiene el formato esperado"

def test_read_jpg_file():
    path = "data/sample.jpg"  # Asegúrate de que esta ruta sea correcta para tu archivo JPG de prueba
    img_RGB, img2show = read_jpg_file(path)
    assert img_RGB.shape == (512, 512, 3), "La imagen leída no tiene el formato esperado"

def test_load_trained_model():
    model = load_trained_model()
    assert model is not None, "El modelo no se cargó correctamente"

def test_grad_cam():
    array = np.random.randint(0, 255, (512, 512, 3), dtype=np.uint8)
    model = load_trained_model()
    heatmap = grad_cam(array, model)
    assert heatmap.shape == (512, 512, 3), "El mapa de calor no tiene el tamaño correcto"
    assert heatmap.dtype == np.uint8, "El mapa de calor no tiene el tipo de dato correcto"
