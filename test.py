import pytest
import pandas as pd
from main import categorize_success

def test_categorize_success():
    df = pd.DataFrame({"engagement_score": [100, 50, 200]})
    df["success_label"] = df.apply(lambda row: categorize_success(row), axis=1)
    assert all(df["success_label"].isin([0, 1]))  # Ensure only 0 or 1 labels
