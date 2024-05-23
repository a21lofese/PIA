import pandas as pd
from flask import Flask, jsonify, request
import pickle as pkl

# Cargar el modelo y el preprocesador
with open('C:/Users/sergi/Documents/Estudios/2023/PIA/Examen/RedesNeuronales/california_model.pkl', 'rb') as file:
    model = pkl.load(file)
with open('C:/Users/sergi/Documents/Estudios/2023/PIA/Examen/RedesNeuronales/california_preprocessor.pkl', 'rb') as file:
    preprocessor = pkl.load(file)

# Crear la aplicación
app = Flask(__name__)


# Crear las rutas
@app.route('/')
def home():  # Ruta para la página de inicio
    return "Bienvenido a la API de California."  # Mensaje de bienvenida


# Ruta para la predicción
@app.route('/predict', methods=['POST'])
def predict(): # Función para la predicción
    data = request.get_json() # Obtener los datos del cuerpo de la petición

    # Convertir el diccionario en un DataFrame
    data_df = pd.DataFrame(data, index=[0])

    # Realizar la predicción
    prediction = model.predict(preprocessor.transform(data_df))[0]

    # Convertir la predicción a una cantidad que entendamos
    prediction = round(float(prediction * 100), 3)

    # Devolver la predicción
    return jsonify({'Precio': prediction}), 200


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# JSON:
# {
#     "MedInc" : 8.3252,
#     "HouseAge" : 41.0,
#     "AveRooms" : 6.984127,
#     "AveBedrms" : 1.023810,
#     "Population" : 322.0,
#     "AveOccup" : 2.555556,
#     "Latitude" : 37.88,
#     "Longitude" : -122.23
# }
#
# Output Esperado:
# {
#     "target": 452.600
# }
# Output Recibido:
# {
#     "target": 425.123
# }
