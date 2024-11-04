def test_chart_creation():
    try:
        sns.set(style="darkgrid")
        plt.figure(figsize=(12, 6))
        chart = sns.countplot(
            data=filtered_df, x="platform", hue="genre", order=["PS4", "XOne", "PC", "WiiU"]
        )
        plt.close()  # Close plot after creating
        print("Test passed: Chart created successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

test_chart_creation()
