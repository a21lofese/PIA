from flask import Flask, request, render_template
import pickle
import numpy as np
import cv2

model = pickle.load(open('../Model/model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])
def predict():

    data = request.files['image']
    data.save('upload/image.png')

    img = cv2.imread('upload/image.png')
    img = cv2.resize(img, (28, 28))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = np.expand_dims(img, axis=0) / 255.0

    prediction = np.argmax(model.predict(img))

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
