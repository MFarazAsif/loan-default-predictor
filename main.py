from src.applicant import LoanApplicant

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