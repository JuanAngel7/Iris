# Despliegue de Modelo de Clasificación Iris con Docker y Flask API

Este proyecto demuestra el despliegue de un modelo de Machine Learning entrenado con el clásico conjunto de datos Iris (`modelo.pkl`). El modelo se expone a través de una API RESTful (Flask) y está empaquetado y estandarizado con Docker para garantizar una ejecución consistente en cualquier entorno, incluido [Play with Docker (PWD)](https://labs.play-with-docker.com/).

## 🌷 Modelo Iris y Estructura del Proyecto

El modelo tiene como objetivo clasificar la especie de flor Iris (**Setosa**, **Versicolor**, **Virginica**) basándose en las medidas de sus pétalos y sépalos.

| Archivo           | Función                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `app.py`          | Contiene la lógica de la API (usando Flask). Carga `modelo.pkl` y define el endpoint de predicción. |
| `modelo.pkl`      | El modelo de Machine Learning (ej. Scikit-learn `RandomForestClassifier`) pre-entrenado. |
| `requirements.txt`| Lista las dependencias de Python necesarias (`Flask`, `scikit-learn`, `pandas`). |
| `Dockerfile`      | Define el entorno de la aplicación para Docker y configura el puerto.   |

## ⚙️ Requisitos

- **Docker**: Instalado en tu máquina local para construir y ejecutar contenedores (si deseas probar localmente).
- **Cuenta de Docker Hub**: Necesaria para subir la imagen y facilitar el despliegue en Play with Docker o cualquier servicio en la nube.
- **Repositorio GitHub**: El código fuente debe estar alojado en GitHub para usar la opción de clonación.

## 🚀 Despliegue Local con Docker

Sigue estos pasos para construir la imagen de Docker y ejecutar la API en tu entorno local.

### 1. Construir la Imagen de Docker

Abre tu terminal en el directorio raíz del proyecto y ejecuta el siguiente comando. Reemplaza `tu-usuario-docker` por tu nombre de usuario de Docker Hub y `nombre-proyecto` por el nombre que desees darle a la imagen (ej. `ml-api-demo`).

```bash
docker build -t tu-usuario-docker/nombre-proyecto:latest .
