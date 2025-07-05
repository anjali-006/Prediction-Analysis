from flask import Flask, request
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app, support_credentials=True)

# Load model
with open("mood_pred.pkl", "rb") as file:
    knn_model = pickle.load(file)

# New route: /mood/predict
@app.route("/mood/predict", methods=["POST"])
def predict_mood():
    data = request.get_json()

    # Extract and convert values
    bed_time = float(data['bed_time'])
    quali_ty = float(data['quali_ty'])

    prebed_raw = str(data['prebed_tech']).strip().lower()
    prebed_tech = 1.0 if prebed_raw in ["yes", "1"] else 0.0

    Wake_up = float(data['Wake_up'])

    # Predict mood
    x = [[bed_time, quali_ty, prebed_tech, Wake_up]]
    y_pred = knn_model.predict(x)

    mood_map = {
        0: "HAPPY",
        1: "JOYFUL",
        2: "PEACEFUL",
        3: "SLEEPY"
    }

    result = mood_map.get(y_pred[0], "Unknown mood")
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
