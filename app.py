from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app) 

model = joblib.load(r"crop_Recommend_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.get_json()
    input_df = pd.DataFrame([data])
    
    prediction = model.predict(input_df)[0]
    return jsonify({
        'success': True,
        'crop': str(prediction).capitalize()
    })

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5000)
