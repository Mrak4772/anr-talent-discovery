import pytest
import pandas as pd
from utils import categorize_success

def test_categorize_success():
    # Sample data
    df = pd.DataFrame({"engagement_score": [100, 50, 200, 75, 150]})
    
    # Apply the categorize_success function
    df["success_label"] = df.apply(lambda row: categorize_success(row), axis=1)
    
    # Test the result
    assert all(df["success_label"].isin([0, 1]))  # Ensure only 0 or 1 labels
    assert df["success_label"][0] == 1  # Engagement score 100 should be categorized as 1
    assert df["success_label"][1] == 0  # Engagement score 50 should be categorized as 0
    assert df["success_label"][2] == 1  # Engagement score 200 should be categorized as 1
