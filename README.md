\# AI Loan Default Predictor



A machine learning system that predicts whether a loan applicant

will default, built on 44,000 real Lending Club loan records.



\## What it does

\- Predicts loan default probability in real time

\- REST API endpoint built with FastAPI

\- Interactive dashboard built with Streamlit

\- Trained on real Lending Club financial data



\## Tech stack

Python · Pandas · NumPy · Scikit-learn · PyTorch · 

FastAPI · Streamlit · SQLite · Matplotlib · Seaborn · Git



\## Results

\- Random Forest: 70% accuracy, 57% recall

\- Neural Network: 80% accuracy, 18% recall

\- Chose Random Forest — recall matters more in banking



\## How to run

1\. Install dependencies: pip install -r requirements.txt

2\. Train model: python src/model.py

3\. Start API: python -m uvicorn src.api:app --reload

4\. Start dashboard: python -m streamlit run src/dashboard.py



\## Key finding

Defaulters pay 3% higher interest rates, borrow $1,600 more,

and earn $6,500 less than borrowers who repay successfully.

