import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
import pickle

def load_data():
    df = pd.read_csv('data/clean_loan_data.csv')
    X = df.drop('default', axis=1)
    y = df['default']
    return X, y

def train_model():
    X, y = load_data()

    # Split data — 80% train, 20% test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    # Train Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        class_weight='balanced'
    )
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)

    print("\n--- Model Results ---")
    print(f"Accuracy  : {round(accuracy_score(y_test, y_pred) * 100, 2)}%")
    print(f"Precision : {round(precision_score(y_test, y_pred) * 100, 2)}%")
    print(f"Recall    : {round(recall_score(y_test, y_pred) * 100, 2)}%")
    print(f"F1 Score  : {round(f1_score(y_test, y_pred) * 100, 2)}%")

    print("\n--- Confusion Matrix ---")
    print(confusion_matrix(y_test, y_pred))

    print("\n--- Classification Report ---")
    print(classification_report(y_test, y_pred))

    # Feature importance
    features = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)

    print("\n--- Top Features ---")
    print(features.head(10))

    # Save model
    with open('data/loan_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("\nModel saved to data/loan_model.pkl")

    return model

if __name__ == "__main__":
    train_model()