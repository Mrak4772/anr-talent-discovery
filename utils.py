def categorize_success(row):
    if row['engagement_score'] >= 100:
        return 1
    else:
        return 0

