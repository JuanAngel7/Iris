from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo
model = joblib.load('modelo.pkl')

@app.route('/')
def home():
    return jsonify({
        "message": "API de predicción del conjunto de datos Iris",
        "instructions": "Envía una petición POST a /predict con el cuerpo: {\"features\": [sepal_length, sepal_width, petal_length, petal_width]}"
    })

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return jsonify({
            "message": "Usa POST para enviar datos de entrada.",
            "example": {"features": [5.1, 3.5, 1.4, 0.2]}
        }), 200

    try:
        data = request.json
        if not data or 'features' not in data:
            return jsonify({'error': 'El cuerpo debe contener una clave "features" con una lista de 4 números.'}), 400
        
        features = np.array(data['features']).reshape(1, -1)
        if features.shape[1] != 4:
            return jsonify({'error': 'Se esperan exactamente 4 características (sepal length, sepal width, petal length, petal width).'}), 400
        
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': 'Error interno del servidor.', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
