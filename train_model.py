import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import joblib

data = pd.read_csv('/home/kinkini/house-price-prediction/dataset/houses_clean.csv')


X = data[["area","bedrooms","bathrooms","stories","parking"]]
Y = data["price"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train,Y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(Y_test,predictions)

mse = mean_squared_error(Y_test,predictions)

r2 = r2_score(Y_test,predictions)

print("Model Training Completed!")
print("MAE:",mae)
print("MSE:",mse)
print("R2 Score:",r2)

joblib.dump(model, "model/house_price_model.pkl")

print("Model saved successfully!")