def test_filtered_data():
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    assert set(filtered_df['platform'].unique()) == set(platforms), "Data not filtered correctly!"
    print("Test passed: Data filtered correctly.")

test_filtered_data()
