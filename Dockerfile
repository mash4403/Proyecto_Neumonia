FROM python:3.12.0

# DIRECTORIO DE TRABAJO EN EL CONTENEDOR
WORKDIR /app    

#instalar las dependencias
RUN pip install -r requirements.txt
#copiar el contenido de la carpeta actual al contenedor
COPY . ./
#comando para ejecutar la aplicacion
CMD ["python", "app.py"]
