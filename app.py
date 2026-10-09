from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model
model = joblib.load("model/house_price_model.pkl")


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction
@app.route("/predict", methods=["POST"])
def predict():

    # Get the 5 features used when training the model
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    stories = int(request.form["stories"])
    parking = int(request.form["parking"])

    # IMPORTANT:
    # The model was trained with exactly 5 features
    features = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        parking
    ]]

    # Make prediction
    prediction = model.predict(features)

    # Get predicted price
    price = round(prediction[0], 2)

    # Send prediction back to HTML
    return render_template(
        "index.html",
        prediction=price
    )


if __name__ == "__main__":
    app.run(debug=True)
