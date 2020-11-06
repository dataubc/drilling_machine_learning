import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from joblib import dump, load

app = Flask(__name__)
filename1 = "model_ift.pkl"
filename2 = "model_volume.pkl"

with open(filename1, 'rb') as file:
    model_ift = load(file)
with open(filename2, 'rb') as file:
    model_volume = load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    X_test_new = [x.strip() for x in request.form.values()]
    X_test_new[1] = float(X_test_new[1])
    X_test_new[2] = float(X_test_new[2])
    # final_features = [np.array(int_features)]
    # X_test_new = [x for x in request.form.values()]

    # # print(sgd_clf.predict(X_test_new_count))
    #
    ll = [X_test_new]
    new_data = pd.DataFrame(ll, columns=['Gas', 'Water_content', 'time_minutes'])
    prediction = model_ift.predict(new_data)[0]
    output = round(prediction, 2)

    prediction2 = model_volume.predict(new_data)[0]
    output2 = round(prediction2, 2)

    return render_template('index.html', prediction_text2='Estimated IFT =  {} mN/. Estimated Volume Change '
                                                          'Ratio = {} '.format(output, output2))


if __name__ == "__main__":
    app.run(debug=True)
