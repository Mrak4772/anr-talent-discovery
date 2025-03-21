import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

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

def categorize_success(row):
    # Dummy function to simulate how we categorize success based on engagement score
    if row['engagement_score'] > 100:
        return 1
    else:
        return 0

if __name__ == "__main__":
    train_model()
