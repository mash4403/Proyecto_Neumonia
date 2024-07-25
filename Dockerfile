# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código fuente de la aplicación
COPY . .

# Expone el puerto en el que la aplicación va a correr (por ejemplo, 8080)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
