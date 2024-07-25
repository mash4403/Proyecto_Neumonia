## Hola! Bienvenido a la herramienta para la detección rápida de neumonía

Deep Learning aplicado en el procesamiento de imágenes radiográficas de tórax en formato DICOM con el fin de clasificarlas en 3 categorías diferentes, así:

1. Neumonía Bacteriana

2. Neumonía Viral

3. Sin Neumonía

Aplicación de una técnica de explicación llamada Grad-CAM para resaltar con un mapa de calor las regiones relevantes de la imagen de entrada.

---

## Uso de la herramienta:



A continuación le explicaremos cómo empezar a utilizarla.

Requerimientos necesarios para el funcionamiento:

- Instale Anaconda para Windows siguiendo las siguientes instrucciones:
  https://docs.anaconda.com/anaconda/install/windows/

- Abra Anaconda Prompt y ejecute las siguientes instrucciones:

  conda create -n tf tensorflow

  conda activate tf

  cd UAO-Neumonia

  pip install -r requirements.txt

  python detector_neumonia.py

Uso de la Interfaz Gráfica:

- Uso de la Interfaz Gráfica
Ingrese la cédula del paciente en la caja de texto.
Presione el botón 'Cargar Imagen', seleccione la imagen del explorador de archivos del computador (Imágenes de prueba en Google Drive).
Presione el botón 'Predecir' y espere unos segundos hasta que observe los resultados.
Presione el botón 'Guardar' para almacenar la información del paciente en un archivo Excel con extensión .csv.
Presione el botón 'PDF' para descargar un archivo PDF con la información desplegada en la interfaz.
Presione el botón 'Borrar' si desea cargar una nueva imagen.

---

## Arquitectura de archivos propuesta.

## detector_neumonia.py
Contiene el diseño de la interfaz gráfica utilizando Tkinter. Los botones llaman métodos contenidos en otros scripts.

## integrator.py
Es un módulo que integra los demás scripts y retorna solamente lo necesario para ser visualizado en la interfaz gráfica. Retorna la clase, la probabilidad y una imagen del mapa de calor generado por Grad-CAM.

## read_img.py
Script que lee la imagen en formato DICOM para visualizarla en la interfaz gráfica. Además, la convierte a arreglo para su preprocesamiento.

## preprocess_img.py
Script que recibe el arreglo proveniente de read_img.py, realiza las siguientes modificaciones:

Resize a 512x512
Conversión a escala de grises
Ecualización del histograma con CLAHE
Normalización de la imagen entre 0 y 1
Conversión del arreglo de imagen a formato de batch (tensor)
load_model.py
Script que lee el archivo binario del modelo de red neuronal convolucional previamente entrenado.

 #  grad_cam.py
Script que recibe la imagen y la procesa, carga el modelo, obtiene la predicción y la capa convolucional de interés para obtener las características relevantes de la imagen.

## test_modelo.py
Script para realizar pruebas unitarias del modelo.

## test_prediccion.py
Script para realizar pruebas unitarias de las predicciones del modelo.

#  Dockerfile
Archivo de configuración para crear una imagen Docker de la aplicación.

## app.py
Archivo principal para correr la aplicación Flask en Docker.


---
### Uso de Docker
Para construir y correr la imagen Docker, sigue estos pasos:

Asegúrate de que Docker esté instalado y corriendo en tu máquina.

Navega al directorio del proyecto.

Construye la imagen Docker con el siguiente comando:

sh
Copiar código
docker build -t proyecto_neumonia .
Corre el contenedor Docker con el siguiente comando:

sh
Copiar código
docker run -p 8080:8080 proyecto_neumonia
La aplicación estará disponible en http://localhost:8080.

---

## Acerca del Modelo

La red neuronal convolucional implementada (CNN) es basada en el modelo implementado por F. Pasa, V.Golkov, F. Pfeifer, D. Cremers & D. Pfeifer
en su artículo Efcient Deep Network Architectures for Fast Chest X-Ray Tuberculosis Screening and Visualization.

Está compuesta por 5 bloques convolucionales, cada uno contiene 3 convoluciones; dos secuenciales y una conexión 'skip' que evita el desvanecimiento del gradiente a medida que se avanza en profundidad.
Con 16, 32, 48, 64 y 80 filtros de 3x3 para cada bloque respectivamente.

Después de cada bloque convolucional se encuentra una capa de max pooling y después de la última una capa de Average Pooling seguida por tres capas fully-connected (Dense) de 1024, 1024 y 3 neuronas respectivamente.

Para regularizar el modelo utilizamos 3 capas de Dropout al 20%; dos en los bloques 4 y 5 conv y otra después de la 1ra capa Dense.

## Acerca de Grad-CAM

Es una técnica utilizada para resaltar las regiones de una imagen que son importantes para la clasificación. Un mapeo de activaciones de clase para una categoría en particular indica las regiones de imagen relevantes utilizadas por la CNN para identificar esa categoría.

Grad-CAM realiza el cálculo del gradiente de la salida correspondiente a la clase a visualizar con respecto a las neuronas de una cierta capa de la CNN. Esto permite tener información de la importancia de cada neurona en el proceso de decisión de esa clase en particular. Una vez obtenidos estos pesos, se realiza una combinación lineal entre el mapa de activaciones de la capa y los pesos, de esta manera, se captura la importancia del mapa de activaciones para la clase en particular y se ve reflejado en la imagen de entrada como un mapa de calor con intensidades más altas en aquellas regiones relevantes para la red con las que clasificó la imagen en cierta categoría.

## Proyecto original realizado por:

Miguel A. Saavedra Codigo 2238093
