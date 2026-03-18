import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import pickle


class LoanDefaultNet(nn.Module):

    def __init__(self, input_size):
        super(LoanDefaultNet, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.network(x)


def load_and_prepare_data():
    df = pd.read_csv('data/clean_loan_data.csv')
    X = df.drop('default', axis=1).values
    y = df['default'].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    with open('data/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)
    y_train = torch.FloatTensor(y_train).unsqueeze(1)
    y_test = torch.FloatTensor(y_test).unsqueeze(1)

    return X_train, X_test, y_train, y_test


def train_neural_network():
    print("Loading data...")
    X_train, X_test, y_train, y_test = load_and_prepare_data()

    train_dataset = TensorDataset(X_train, y_train)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True, drop_last=True)

    model = LoanDefaultNet(input_size=X_train.shape[1])
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    print("Training neural network...")
    print("-" * 40)

    epochs = 20
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        for X_batch, y_batch in train_loader:
            optimizer.zero_grad()
            y_pred = model(X_batch)
            loss = criterion(y_pred, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        if (epoch + 1) % 5 == 0:
            print(f"Epoch {epoch+1}/{epochs} — Loss: {round(total_loss/len(train_loader), 4)}")

    model.eval()
    with torch.no_grad():
        y_pred_prob = model(X_test)
        y_pred = (y_pred_prob >= 0.5).float()

    y_test_np = y_test.numpy()
    y_pred_np = y_pred.numpy()

    print("\n--- Neural Network Results ---")
    print(classification_report(y_test_np, y_pred_np))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test_np, y_pred_np))

    torch.save(model.state_dict(), 'data/neural_network.pth')
    print("\nNeural network saved to data/neural_network.pth")

    return model


if __name__ == "__main__":
    train_neural_network()