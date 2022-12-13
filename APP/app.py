import flask
from flask import render_template
import pickle
import sklearn
from sklearn import datasets
from tensorflow import keras
import numpy as np
def set_params(y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12):

    model = keras.models.load_model("model.pkl")
    prediction = model.predict([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12])
    return prediction[0][0]

app = flask.Flask(__name__, template_folder = 'templates')
@app.route('/', methods = ['POST', 'GET'])
#@app.route('/index', methods = ['POST', 'GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('main.html')

    if flask.request.method == 'POST':
        with open ('model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)
            
            param_lst = []
            message = ''
            for i in range(1,13,1):
               param = flask.request.form.get(f'y{i}')
               param_lst.append(float(param))
            
            message = set_params(*param_lst)


            return render_template('main.html', result = message)

if __name__== '__main__':
    app.run()