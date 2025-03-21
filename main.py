import pandas as pd
import sqlite3
from sklearn.ensemble import RandomForestClassifier

# Connect to a sample SQLite database
conn = sqlite3.connect("talent_data.db")
df = pd.read_sql("SELECT * FROM artist_engagement", conn)

# Feature Engineering: Calculate engagement score
df["engagement_score"] = df["streams"] * 0.4 + df["likes"] * 0.3 + df["shares"] * 0.2 + df["followers_growth"] * 0.1

# Define success label
def categorize_success(row):
    return 1 if row["engagement_score"] > df["engagement_score"].median() else 0

df["success_label"] = df.apply(categorize_success, axis=1)

# Train Model
X = df[["engagement_score"]]
y = df["success_label"]
model = RandomForestClassifier()
model.fit(X, y)

# Export results
df[["artist_id", "engagement_score", "success_label"]].to_csv("talent_scoring_results.csv", index=False)
print("✅ Results saved to talent_scoring_results.csv")
