def test_grouped_data():
    grouped_data = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
    assert not grouped_data.empty, "Grouped data is empty!"
    assert 'PS4' in grouped_data.index and 'Action' in grouped_data.columns, "Grouping incorrect or missing values!"
    print("Test passed: Data grouped correctly.")

test_grouped_data()
