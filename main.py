from src.applicant import LoanApplicant
import pickle
import numpy as np

# Stage 1 — OOP applicants
applicant_1 = LoanApplicant(
    name="Sarah Ahmed",
    age=34,
    income=75000,
    loan_amount=20000,
    credit_score=720,
    employment_years=5
)

applicant_2 = LoanApplicant(
    name="James Okafor",
    age=27,
    income=32000,
    loan_amount=18000,
    credit_score=560,
    employment_years=0.5
)

applicant_1.summary()
applicant_2.summary()

# Stage 5 — ML prediction
print("\n--- ML Model Prediction ---")

with open('data/loan_model.pkl', 'rb') as f:
    model = pickle.load(f)

applicant = np.array([[
    15000,   # loan_amnt
    14.5,    # int_rate
    450.0,   # installment
    55000,   # annual_inc
    28.5,    # dti
    670,     # fico_range_low
    674,     # fico_range_high
    8,       # open_acc
    12000,   # revol_bal
    55.0,    # revol_util
    22,      # total_acc
    1,       # mort_acc
    0        # pub_rec
]])

prediction = model.predict(applicant)
probability = model.predict_proba(applicant)

print(f"Default prediction : {'YES - High Risk' if prediction[0] == 1 else 'NO - Low Risk'}")
print(f"Default probability: {round(probability[0][1] * 100, 2)}%")