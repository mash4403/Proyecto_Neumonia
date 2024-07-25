import unittest
from tensorflow.keras.models import load_model

class TestLoadModel(unittest.TestCase):
    def setUp(self):
        # Se ejecuta antes de cada prueba
        self.model_path = '/Users/miguelangel/Downloads/conv_MLP_84.h5'

    def test_load_model(self):
        """Prueba que el modelo se cargue correctamente"""
        try:
            model = load_model(self.model_path)
            self.assertIsNotNone(model, "El modelo no se cargó correctamente")
        except Exception as e:
            self.fail(f"Fallo al cargar el modelo: {e}")

if __name__ == '__main__':
    unittest.main()
