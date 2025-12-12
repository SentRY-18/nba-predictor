from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "NBA Predictor API running"}

@app.post("/predict/match")
def predict_match(payload: dict):
    return {"message": "Prediction endpoint not implemented yet"}