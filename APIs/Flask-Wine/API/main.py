from flask import Flask, jsonify, request, render_template
import pickle

model = pickle.load(open('../Model/wine_model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # data = request.get_json()
    data = request.form

    data_to_predict = [[
        float(data['fixed_acidity']),
        float(data['volatile_acidity']),
        float(data['citric_acid']),
        float(data['residual_sugar']),
        float(data['chlorides']),
        float(data['free_sulfur_dioxide']),
        float(data['total_sulfur_dioxide']),
        float(data['density']),
        float(data['pH']),
        float(data['sulphates']),
        float(data['alcohol'])
    ]]

    prediction = model.predict(data_to_predict).item()

    # return jsonify({'prediction': prediction}), 200
    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
