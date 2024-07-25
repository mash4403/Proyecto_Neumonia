# Prueba unitaria para verificar que el modelo pueda hacer una predicción
import unittest
import numpy as np
from tensorflow.keras.models import load_model

class TestModelPrediction(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.model_path = '/Users/miguelangel/Downloads/conv_MLP_84.h5'
        self.model = load_model(self.model_path)

    def test_model_prediction(self):
        """Prueba que el modelo pueda hacer una predicción"""
        # Crear una imagen de prueba (una matriz de ceros con la forma correcta)
        test_image = np.zeros((1, 512, 512, 1))
        
        try:
            prediction = self.model.predict(test_image)
            self.assertIsNotNone(prediction, "La predicción es None")
            self.assertEqual(prediction.shape[0], 1, "La predicción no tiene el tamaño correcto")
        except Exception as e:
            self.fail(f"Fallo al hacer la predicción: {e}")

if __name__ == '__main__':
    unittest.main()
