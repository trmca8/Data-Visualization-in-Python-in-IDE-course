import pandas as pd

def test_grouped_data():
    data_path = "../../dataset.csv" 
    df = pd.read_csv(data_path) 
    
    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    
    grouped_data = filtered_df.groupby(['platform', 'genre']).size().unstack(fill_value=0)
    
    assert not grouped_data.empty, "Grouped data is empty!"
    assert 'PS4' in grouped_data.index and 'Action' in grouped_data.columns, "Grouping incorrect or missing values!"
    print("Test passed: Data grouped correctly.")

test_grouped_data()

