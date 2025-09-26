import numpy as np
from flask import Flask, request, render_template, jsonify
import joblib



# Create flask app
flask_app = Flask(__name__)
model = joblib.load(open("trained_model_rf.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict/api", methods=["POST"])
def predict_api():
    data1 = float(request.form['age'])
    data2 = float(request.form['anaemia'])
    data3 = float(request.form['creatinine_phosphokinase'])
    data4 = float(request.form['diabetes'])
    data5 = float(request.form['ejection_fraction'])
    data6 = float(request.form['high_blood_pressure'])
    data7 = float(request.form['platelets'])
    data8 = float(request.form['serum_creatinine'])
    data9 = float(request.form['serum_sodium'])
    data10 = float(request.form['sex'])
    data11 = float(request.form['smoking'])
    data12 = float(request.form['time'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]])

    pred = model.predict(arr)

    return jsonify({'prediction': int(pred[0])})  # Convert prediction to int for JSON compatibility

@flask_app.route("/predict", methods=["POST"])
def predict():
    data1 = float(request.form['age'])
    data2 = float(request.form['anaemia'])
    data3 = float(request.form['creatinine_phosphokinase'])
    data4 = float(request.form['diabetes'])
    data5 = float(request.form['ejection_fraction'])
    data6 = float(request.form['high_blood_pressure'])
    data7 = float(request.form['platelets'])
    data8 = float(request.form['serum_creatinine'])
    data9 = float(request.form['serum_sodium'])
    data10 = float(request.form['sex'])
    data11 = float(request.form['smoking'])
    data12 = float(request.form['time'])
    arr = np.array([[data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12]])

    pred = model.predict(arr)

    return render_template("index.html", prediction_text="Prediksi penyakit adalah {}".format(int(pred[0])))

if __name__ == "__main__":
    flask_app.run(debug=True)
