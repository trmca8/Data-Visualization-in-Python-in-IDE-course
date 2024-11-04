import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data_path = "./dataset.csv"
df = pd.read_csv(data_path)

# Set the style to match the example chart
sns.set(style="darkgrid")

# Create the plot
plt.figure(figsize=(12, 6))
chart = sns.countplot(
    data=df, x="platform", hue="genre", order=["PS4", "XOne", "PC", "WiiU"]
)

# Adjust the legend
plt.legend(title='genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel("platform")
plt.ylabel("count")
plt.title("")

# Display the plot
plt.tight_layout()
plt.show()
