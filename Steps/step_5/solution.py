# Solution for customizing the chart
plt.figure(figsize=(12, 6))
chart = sns.countplot(
    data=filtered_df, x="platform", hue="genre", order=["PS4", "XOne", "PC", "WiiU"]
)

# Adding labels and adjusting legend
plt.xlabel("platform")
plt.ylabel("count")
plt.legend(title='genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Display the final chart
plt.show()
