import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize Flask application
application = Flask(__name__)
app = application

# Load ridge regression model and scaler with error handling
try:
    ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
    standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))
except FileNotFoundError as e:
    print(f"Error: {e}")
    ridge_model, standard_scaler = None, None
except Exception as e:
    print(f"Unexpected error: {e}")
    ridge_model, standard_scaler = None, None

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for prediction form
@app.route('/predict')
def predict():
    return render_template('home.html')

# Route to handle prediction data
@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        # Get input data from form
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Ensure scaler and model are loaded
        if not ridge_model or not standard_scaler:
            return render_template('home.html', result="Model or Scaler not loaded.")

        # Transform input data and make predictions
        new_data_scaled = standard_scaler.transform(
            [[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]]
        )
        result = ridge_model.predict(new_data_scaled)

        # Return result to template
        return render_template('home.html', result=result[0])

    except ValueError:
        return render_template('home.html', result="Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"Error during prediction: {e}")
        return render_template('home.html', result="An error occurred during prediction.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
