from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

# Cargar el modelo y el preprocesador desde archivos
with open('../model/model.pkl', 'rb') as file:
    model = pickle.load(file)
    preprocessor = pickle.load(file)
    df_columns = pickle.load(file)

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
        data['DoNotCall'],
        float(data['TotalVisits']),
        int(data['TotalTimeSpentonWebsite']),
        float(data['PageViewsPerVisit']),
        data['LastActivity'],
        data['Country'],
        data['Specialization'],
        data['HowdidyouhearaboutXEducation'],
        data['Whatisyourcurrentoccupation'],
        data['Whatmattersmosttoyouinchoosingacourse'],
        data['Search'],
        data['NewspaperArticle'],
        data['XEducationForums'],
        data['Newspaper'],
        data['DigitalAdvertisement'],
        data['ThroughRecommendations'],
        data['Tags'],
        data['LeadQuality'],
        data['LeadProfile'],
        data['City'],
        data['AsymmetriqueActivityIndex'],
        data['AsymmetriqueProfileIndex'],
        float(data['AsymmetriqueActivityScore']),
        float(data['AsymmetriqueProfileScore']),
        data['AfreecopyofMasteringTheInterview'],
        data['LastNotableActivity']
    ]], columns=[
        "LeadOrigin", "LeadSource", "DoNotEmail", "DoNotCall", "TotalVisits", "TotalTimeSpentonWebsite",
        "PageViewsPerVisit", "LastActivity", "Country", "Specialization", "HowdidyouhearaboutXEducation",
        "Whatisyourcurrentoccupation", "Whatmattersmosttoyouinchoosingacourse", "Search", "NewspaperArticle",
        "XEducationForums", "Newspaper", "DigitalAdvertisement", "ThroughRecommendations", "Tags", "LeadQuality",
        "LeadProfile", "City", "AsymmetriqueActivityIndex", "AsymmetriqueProfileIndex", "AsymmetriqueActivityScore",
        "AsymmetriqueProfileScore", "AfreecopyofMasteringTheInterview", "LastNotableActivity"
    ])

    # Realizar el preprocesamiento de los datos
    data_to_predict = preprocessor.transform(data_to_predict)

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(data_to_predict)[0]
    prediction = 'El cliente si se convertirá' if prediction == 1 else 'El cliente no se convertirá'

    # Devolver la predicción a la plantilla HTML
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
