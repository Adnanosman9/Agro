from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pandas as pd
import joblib

APP_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=APP_DIR, static_url_path="")
CORS(app)

model = joblib.load(os.path.join(APP_DIR, "crop_Recommend_model.pkl"))

@app.route("/")
def home():
    return send_from_directory(APP_DIR, "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]
    return jsonify({
        "success": True,
        "crop": str(prediction).capitalize()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
