class LoanApplicant:

    def __init__(self, name, age, income, loan_amount, credit_score, employment_years):
        self.name = name
        self.age = age
        self.income = income
        self.loan_amount = loan_amount
        self.credit_score = credit_score
        self.employment_years = employment_years

    def debt_to_income_ratio(self):
        return round(self.loan_amount / self.income, 2)

    def is_eligible(self):
        if self.credit_score < 580:
            return False, "Credit score too low"
        if self.debt_to_income_ratio() > 0.4:
            return False, "Debt-to-income ratio too high"
        if self.employment_years < 1:
            return False, "Insufficient employment history"
        return True, "Eligible for review"

    def risk_category(self):
        score = self.credit_score
        if score >= 750:
            return "A — Very Low Risk"
        elif score >= 700:
            return "B — Low Risk"
        elif score >= 650:
            return "C — Medium Risk"
        elif score >= 600:
            return "D — High Risk"
        else:
            return "F — Very High Risk"
        
    def monthly_payment(self, repayment_years):
             return round(self.loan_amount / (repayment_years * 12), 2)

    def summary(self):
        eligible, reason = self.is_eligible()
        print("=" * 40)
        print(f"  Applicant     : {self.name}")
        print(f"  Income        : ${self.income:,}")
        print(f"  Loan Amount   : ${self.loan_amount:,}")
        print(f"  Credit Score  : {self.credit_score}")
        print(f"  DTI Ratio     : {self.debt_to_income_ratio()}")
        print(f"  Risk Category : {self.risk_category()}")
        print(f"  Eligibility   : {reason}")
        print(f"  Monthly Payment: ${self.monthly_payment(5):,}")
        print("=" * 40)