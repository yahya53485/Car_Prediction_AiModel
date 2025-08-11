import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib

# 📂 Load dataset
data = pd.read_csv("D:\Coding\car_prediction\Dataset\cardekho_dataset.csv")
print("✅ Columns loaded:", data.columns.tolist())

# 🧹 Drop NaN values
data.dropna(inplace=True)

# 🛠 Extract numeric values where needed
def extract_numeric(val):
    try:
        return float(str(val).split()[0])
    except:
        return np.nan

data['mileage'] = data['mileage'].apply(extract_numeric)
data['engine'] = data['engine'].apply(extract_numeric)
data['max_power'] = data['max_power'].apply(extract_numeric)

# 📌 Categorical columns
categorical_columns = ['brand', 'model', 'seller_type', 'fuel_type', 'transmission_type']
label_encoders = {}

for col in categorical_columns:
    if col in data.columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col].astype(str))
        label_encoders[col] = le
    else:
        print(f"⚠️ Column '{col}' not found!")

# 🧹 Drop any NaN left after processing
data.dropna(inplace=True)

# 🎯 Features & Target
X = data[['brand', 'model', 'vehicle_age', 'km_driven', 
          'seller_type', 'fuel_type', 'transmission_type',
          'mileage', 'engine', 'max_power', 'seats']]

y = data['selling_price']

# 📏 Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✂️ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 🤖 Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 🔮 Predictions
y_pred = model.predict(X_test)

# 📊 Evaluation
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"🎯 R² Score: {round(r2 * 100, 2)}%")
print(f"📉 MAE: ₹{round(mae, 2)}")
print(f"📉 RMSE: ₹{round(rmse, 2)}")

# 💾 Save everything
joblib.dump(model, "car_model.joblib")
joblib.dump(scaler, "scaler.joblib")
joblib.dump(label_encoders, "encoders.joblib")

print("✅ Saved: car_model.joblib, scaler.joblib, encoders.joblib")
