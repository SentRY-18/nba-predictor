import sys, os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(ROOT)

DATA_PATH = "data/processed/games.csv"
MODEL_PATH = "models/winner_model.joblib"

def main():
    df = pd.read_csv(DATA_PATH)

    df["WIN_HOME"] = (df["HOME_TEAM_SCORE"] > df["VISITOR_TEAM_SCORE"]).astype(int)

    X = df[["HOME_TEAM_ID", "VISITOR_TEAM_ID"]]
    y = df["WIN_HOME"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    print(f"Accuracy : {acc:.3f}")

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"✔ Modèle sauvegardé : {MODEL_PATH}")


if __name__ == "__main__":
    main()