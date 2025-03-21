import pandas as pd
import matplotlib.pyplot as plt

# Load data (you can load from a CSV or database)
df = pd.DataFrame({"engagement_score": [100, 50, 200, 75, 150], "success_label": [1, 0, 1, 0, 1]})

# Plot the data
plt.figure(figsize=(8,6))
plt.bar(df['engagement_score'], df['success_label'], color='blue')
plt.xlabel('Engagement Score')
plt.ylabel('Success Label')
plt.title('Engagement Score vs Success Label')

# Save the plot as an image
plt.savefig('engagement_vs_success.png')
plt.close()
