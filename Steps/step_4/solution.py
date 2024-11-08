# Solution for creating the grouped bar chart
sns.set(style="darkgrid")
plt.figure(figsize=(12, 6))
chart = sns.countplot(
    data=filtered_df, x="platform", hue="genre", order=["PS4", "XOne", "PC", "WiiU"]
)
plt.show()
