# Propósito: Proporciona funciones para leer y preprocesar imágenes.
# Contenido:
 # read_dicom_file(path): Lee y preprocesa archivos DICOM.

import pydicom
from PIL import Image
import numpy as np
import cv2

def read_dicom_file(path):
    img = pydicom.dcmread(path)
    img_array = img.pixel_array
    img2show = Image.fromarray(img_array)
    img2 = img_array.astype(float)
    img2 = (np.maximum(img2, 0) / img2.max()) * 255.0
    img2 = np.uint8(img2)
    img_RGB = cv2.cvtColor(img2, cv2.COLOR_GRAY2RGB)
    return img_RGB, img2show
