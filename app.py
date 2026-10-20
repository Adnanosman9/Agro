from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib
import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

model_path = os.path.join(os.path.dirname(__file__), "crop_Recommend_model.pkl")
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True)
    fields = ('N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall')

    try:
        if not isinstance(data, dict):
            raise ValueError('Send a JSON object with the crop parameters.')
        input_df = pd.DataFrame([{field: float(data[field]) for field in fields}])
        prediction = model.predict(input_df)[0]
    except (KeyError, TypeError, ValueError) as error:
        return jsonify(success=False, error=f'Invalid input: {error}'), 400
    except Exception:
        app.logger.exception('Prediction failed')
        return jsonify(success=False, error='Prediction could not be completed.'), 500

    return jsonify(success=True, crop=str(prediction).capitalize())

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
