import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils import categorize_success

def train_model():
    # Load the data
    df = pd.read_csv('data/talent_data.csv')
    
    # Features and Labels
    X = df[['engagement_score']]
    y = df['success_label']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Model training
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Predictions
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Model Accuracy: {accuracy * 100:.2f}%")
    
    return model

if __name__ == "__main__":
    train_model()
