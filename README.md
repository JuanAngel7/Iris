Despliegue de Modelo de Clasificación Iris con Docker y Flask API

Este proyecto demuestra el despliegue de un modelo de Machine Learning entrenado con el clásico conjunto de datos Iris (modelo.pkl). El modelo se expone a través de una API RESTful (Flask) y está empaquetado y estandarizado con Docker para garantizar una ejecución consistente en cualquier entorno, incluido Play with Docker (PWD).

🌷 Modelo Iris y Estructura del Proyecto

El modelo tiene como objetivo clasificar la especie de flor Iris (Setosa, Versicolor, Virginica) basándose en las medidas de sus pétalos y sépalos.

Archivo

Función

app.py

Contiene la lógica de la API (usando Flask). Carga modelo.pkl y define el endpoint de predicción.

modelo.pkl

El modelo de Machine Learning (ej. Scikit-learn RandomForestClassifier) pre-entrenado.

requirements.txt

Lista las dependencias de Python necesarias (Flask, scikit-learn, pandas).

Dockerfile

Define el entorno de la aplicación para Docker.as y configurando el puerto.

⚙️ Requisitos

Docker: Instalado en tu máquina local para construir y ejecutar contenedores (si deseas probar localmente).

Cuenta de Docker Hub: Necesaria para subir la imagen y facilitar el despliegue en Play with Docker o cualquier servicio en la nube.

Repositorio GitHub: El código fuente debe estar alojado en GitHub para usar la opción de clonación.

🚀 Despliegue Local con Docker

Sigue estos pasos para construir la imagen de Docker y ejecutar la API en tu entorno local.

1. Construir la Imagen de Docker

Abre tu terminal en el directorio raíz del proyecto y ejecuta el siguiente comando. Reemplaza tu-usuario-docker por tu nombre de usuario de Docker Hub y nombre-proyecto por el nombre que desees darle a la imagen (ej. ml-api-demo).

docker build -t tu-usuario-docker/nombre-proyecto:latest .



2. Ejecutar el Contenedor

Una vez construida la imagen, ejecuta el contenedor mapeando el puerto interno (8080, según el Dockerfile) al puerto 8080 de tu máquina local:

docker run -p 8080:8080 tu-usuario-docker/nombre-proyecto:latest



3. Probar la API

La API estará disponible en http://localhost:8080. Puedes probar el endpoint de predicción (asumiendo que es /predict) enviando una solicitud POST.

🌐 Despliegue en Play with Docker (PWD)

PWD es un entorno de laboratorio gratuito que permite ejecutar Docker en línea. Aquí presentamos dos métodos de despliegue en PWD:

Método A: Usar Imagen Pre-construida de Docker Hub (Recomendado para producción)

Este método es el más rápido ya que evita la construcción y solo descarga y ejecuta la imagen.

Subir la Imagen a Docker Hub (si no lo has hecho):

docker login
docker push tu-usuario-docker/nombre-proyecto:latest



Ejecutar en PWD: Inicia una nueva sesión en PWD y ejecuta el siguiente comando.

docker run -d -p 80:8080 tu-usuario-docker/nombre-proyecto:latest



Método B: Clonar y Construir Directamente en PWD (Común en entornos de laboratorio)

Este método simula un flujo de trabajo de desarrollo donde se clona el código fuente para construir la imagen in situ.

Clonar el Repositorio GitHub: Reemplaza URL_DEL_REPO con la URL HTTPS de tu repositorio.

git clone URL_DEL_REPO



Acceder al Directorio:

cd nombre-del-repositorio-clonado



Construir la Imagen en PWD: Usa el comando docker build para crear la imagen dentro del entorno PWD.

docker build -t ml-api-pwd:latest .



Ejecutar el Contenedor: Ejecuta la imagen recién construida, mapeando el puerto 80 al puerto 8080 del contenedor.

docker run -d -p 80:8080 ml-api-pwd:latest



Nota General: Una vez que el contenedor esté corriendo, PWD mostrará un enlace o un botón para acceder al puerto expuesto (en este caso, el puerto 80) y probar tu API en línea.

📝 Contenido del Dockerfile (Referencia)

Para referencia, este es el rol que cumplen las instrucciones en el Dockerfile:

# Usa una imagen base de Python ligera
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requisitos e instálalos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos al directorio de trabajo
COPY . .

# Expone el puerto que usará la aplicación Flask
EXPOSE 8080

# Comando para iniciar la aplicación Flask cuando el contenedor se ejecute
CMD ["python", "app.py"]

