from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/house_price_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')    

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    stories = int(request.form['stories'])
    parking = int(request.form['parking'])

    features = [[area, bedrooms, bathrooms, stories, parking]]

    prediction = model.predict(features)

    price = round(prediction[0], 2)

    return render_template('index.html', prediction_text=f'The predicted price for the house is: ${price:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)