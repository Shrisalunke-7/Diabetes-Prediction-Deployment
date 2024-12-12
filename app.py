# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest Classifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

# Home route to display the form
@app.route('/')
def home():
    return render_template('index.html')

# Predict route to handle form submission and display prediction
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extracting input data from the form
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])

            # Prepare the input data for prediction
            data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])

            # Predict using the loaded model
            my_prediction = classifier.predict(data)

            # Render the result page with prediction
            return render_template('result.html', prediction=my_prediction[0])

        except Exception as e:
            # If there is an error, display a generic error message
            return render_template('result.html', prediction="Error: Unable to make a prediction. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
