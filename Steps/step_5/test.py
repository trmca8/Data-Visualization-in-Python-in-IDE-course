def test_customization():
    try:
        plt.figure(figsize=(12, 6))
        chart = sns.countplot(
            data=filtered_df, x="platform", hue="genre", order=["PS4", "XOne", "PC", "WiiU"]
        )
        plt.xlabel("platform")
        plt.ylabel("count")
        plt.legend(title='genre', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.close()  # Close plot after creating
        print("Test passed: Customization applied successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

test_customization()
