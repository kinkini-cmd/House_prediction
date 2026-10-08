import joblib
import pandas as pd


model = joblib.load("model/house_price_model.pkl")

house = pd.DataFrame({
    "area": [2500],
    "bedrooms": [4],
    "bathrooms": [3],
    "stories": [2],
    "parking": [2]
})
predicted_price = model.predict(house)
print(f"The predicted price for the house is: ${predicted_price[0]:,.2f}")