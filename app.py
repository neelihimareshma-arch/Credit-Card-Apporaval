from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_card_model.pkl")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':

        try:

            # Read all form values
            features = [float(x) for x in request.form.values()]

            # Convert into numpy array
            final_features = np.array(features).reshape(1, -1)

            # Prediction
            prediction = model.predict(final_features)

            if prediction[0] == 1:
                result = "Fraud Transaction"
            else:
                result = "Non-Fraud Transaction"

            return render_template("result.html", prediction=result)

        except Exception as e:
            return render_template("result.html", prediction=str(e))

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)