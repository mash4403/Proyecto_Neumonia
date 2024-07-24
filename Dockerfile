
#
# Utilizar una imagen base de Python
FROM python:3.12.0

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del contenido de la carpeta actual al contenedor
COPY . .

# Exponer el puerto que utiliza la aplicación
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "detector_neumonia.py"]
