from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

# Cargar el modelo y el preprocesador desde archivos
model = pickle.load(open('../model/model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.form

    # Convertir los datos del formulario en un DataFrame
    data_to_predict = pd.DataFrame([[
        data['LeadOrigin'],
        data['LeadSource'],
        data['DoNotEmail'],
        data['TotalTimeSpentOnWebsite'],
        data['LastActivity'],
        data['Specialization'],
        data['WhatIsYourCurrentOccupation'],
        data['Tags'],
        data['LeadQuality'],
        data['LeadProfile'],
        data['City'],
        data['AsymmetriqueActivityIndex'],
        data['AsymmetriqueProfileIndex'],
        data['LastNotableActivity']
    ]], columns=[
        'LeadOrigin',  # string
        'LeadSource',  # string
        'DoNotEmail',  # string
        'TotalTimeSpentOnWebsite',  # int
        'LastActivity',  # string
        'Specialization',  # string
        'WhatIsYourCurrentOccupation',  # string
        'Tags',  # string
        'LeadQuality',  # string
        'LeadProfile',  # string
        'City',  # string
        'AsymmetriqueActivityIndex',  # string
        'AsymmetriqueProfileIndex',  # string
        'LastNotableActivity'  # string
    ])

    # Realizar el preprocesamiento de los datos
    encoder = OrdinalEncoder()
    # Solo se transforma las columnas categóricas
    for column in data_to_predict.select_dtypes(include=['object']).columns:
        data_to_predict[column] = encoder.fit_transform(data_to_predict[[column]])

    # Escalar los datos
    scaler = StandardScaler()
    data_to_predict = scaler.fit_transform(data_to_predict)

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(data_to_predict)[0]
    prediction = 'Sí' if prediction else 'No'

    # Devolver la predicción a la plantilla HTML
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
