from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI(title="Loan Default Predictor API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'data', 'loan_model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

class LoanApplication(BaseModel):
    loan_amnt: float
    int_rate: float
    installment: float
    annual_inc: float
    dti: float
    fico_range_low: float
    fico_range_high: float
    open_acc: float
    revol_bal: float
    revol_util: float
    total_acc: float
    mort_acc: float
    pub_rec: float

@app.get("/")
def home():
    return {"message": "Loan Default Predictor API is running"}

@app.post("/predict")
def predict(application: LoanApplication):
    data = np.array([[
        application.loan_amnt,
        application.int_rate,
        application.installment,
        application.annual_inc,
        application.dti,
        application.fico_range_low,
        application.fico_range_high,
        application.open_acc,
        application.revol_bal,
        application.revol_util,
        application.total_acc,
        application.mort_acc,
        application.pub_rec
    ]])

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]

    return {
        "default_prediction": int(prediction),
        "default_probability": round(float(probability) * 100, 2),
        "risk_level": "High Risk" if probability > 0.5 else "Low Risk",
        "recommendation": "Reject" if probability > 0.5 else "Review"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}