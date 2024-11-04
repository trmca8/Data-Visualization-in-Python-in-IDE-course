import pandas as pd

def test_data_loaded():
    data_path = "path/to/dataset.csv"
    df = pd.read_csv(data_path)
    assert not df.empty, "DataFrame is empty!"
    print("Test passed: Data loaded successfully.")

test_data_loaded()
