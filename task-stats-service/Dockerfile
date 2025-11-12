# Usamos una imagen oficial de Python
FROM python:3.12-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos del proyecto al contenedor
COPY . .

# Instalamos dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponemos el puerto (Django por defecto usa 8000)
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]