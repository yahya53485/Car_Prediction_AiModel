from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

# Initialize app
app = Flask(__name__)

# Load saved model and preprocessing tools
model = joblib.load("car_model.joblib")
scaler = joblib.load("scaler.joblib")
label_encoders = joblib.load("encoders.joblib")

# Feature order exactly same as training
feature_order = ['brand', 'model', 'vehicle_age', 'km_driven', 
                 'seller_type', 'fuel_type', 'transmission_type',
                 'mileage', 'engine', 'max_power', 'seats']

@app.route('/')
def home():
    return render_template('index.html')  # form input page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1️⃣ Get form data
        input_data = {
            'brand': request.form['brand'],
            'model': request.form['model'],
            'vehicle_age': float(request.form['vehicle_age']),
            'km_driven': float(request.form['km_driven']),
            'seller_type': request.form['seller_type'],
            'fuel_type': request.form['fuel_type'],
            'transmission_type': request.form['transmission_type'],
            'mileage': float(request.form['mileage']),
            'engine': float(request.form['engine']),
            'max_power': float(request.form['max_power']),
            'seats': float(request.form['seats'])
        }

        # 2️⃣ Encode categorical features safely
        for col in label_encoders:
            if col in input_data:
                if input_data[col] in label_encoders[col].classes_:
                    input_data[col] = label_encoders[col].transform([input_data[col]])[0]
                else:
                    return f"❌ Error: Unknown category '{input_data[col]}' for column '{col}'"

        # 3️⃣ Create DataFrame in correct feature order and scale
        input_df = pd.DataFrame([[input_data[col] for col in feature_order]], columns=feature_order)
        input_scaled = scaler.transform(input_df)

        # 4️⃣ Predict
        prediction = model.predict(input_scaled)[0]
        predicted_price = round(prediction, 2)

        # 5️⃣ Render result
        return render_template('result.html', prediction=f"Predicted Price: ₹{predicted_price}")

    except Exception as e:
        return f"❌ Error occurred: {e}"

# 🚀 Run the app
if __name__ == '__main__':
    app.run(debug=True)
