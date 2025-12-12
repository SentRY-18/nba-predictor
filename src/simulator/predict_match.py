import sys, os
import joblib
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ROOT)

MODEL_PATH = os.path.join(ROOT, "models", "winner_model.joblib")

def load_model():
    print("→ Loading model at:", MODEL_PATH)
    return joblib.load(MODEL_PATH)

def predict_match(home_id, visitor_id):
    model = load_model()

    X = pd.DataFrame([{
        "HOME_TEAM_ID": int(home_id),
        "VISITOR_TEAM_ID": int(visitor_id)
    }])

    return model.predict_proba(X)[0][1]


if __name__ == "__main__":
    home = 1610612747
    away = 1610612744

    p = predict_match(home, away)
    print(f"Probabilité de victoire domicile : {p:.2f}")