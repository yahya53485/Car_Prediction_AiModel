# 🚗💨 AI-Powered Car Price Prediction

> *"Guess the price of any used car like a pro dealer… but smarter 🤖"*  

[![Python](https://img.shields.io/badge/Python-3.9+-FFD43B?logo=python&logoColor=blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask)](https://flask.palletsprojects.com/)  
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)  
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://your-render-link-here)

---

## 🛠 What This App Does
This web app takes your car’s details like:
- Brand & Model
- Vehicle Age
- Mileage
- Fuel Type
- Transmission  
...and predicts its **fair market value** 💰 using Machine Learning.

📍 **Live Demo:** [Try it now](https://your-render-link-here)

---

## 📸 Quick Peek  
**Home Page:**  
![Home](static/home_preview.png)  

**Prediction Page:**  
![Result](static/result_preview.png)

---

## 🧠 How It Works
1. **Data Cleaning & Feature Engineering** 🧹  
   - Handles missing values  
   - Encodes categorical features (brand, model, etc.)  
   - Scales numerical values (mileage, engine, etc.)  
   
2. **Model Training** 🤓  
   - Algorithm: Random Forest Regressor 🌲  
   - Evaluated with MAE, RMSE, and R² Score  

3. **Deployment** 🚀  
   - Flask backend  
   - Hosted on Render  

---

## 📂 Repo Layout

📦 Car-Price-Prediction
┣ 📂 static/ # CSS, JS, and assets
┣ 📂 templates/ # HTML templates
┣ 📜 app.py # Flask app
┣ 📜 model_building.py
┣ 📜 car_model.joblib
┣ 📜 encoders.joblib
┣ 📜 scaler.joblib
┣ 📜 requirements.txt
┗ 📜 README.md



---

## 💻 Run Locally
```bash
# Clone the repository
git clone https://github.com/your-username/car-price-prediction.git
cd car-price-prediction

# Install dependencies
pip install -r requirements.txt

# Start the app
python app.py


Then open http://127.0.0.1:5000 in your browser 🌐

📊 Dataset Info
Source: Cardekho.com

Size: ~8k rows

Features: brand, model, year, mileage, engine, max power, fuel type, seller type, transmission, seats.

🎯 Future Upgrades
Add API endpoint for mobile app integration 📱

Multiple models & accuracy comparison 📊

Fancy dashboard UI with charts 📈

💬 Connect with Me
💌 Email: your.email@example.com
🌐 GitHub: your-username

