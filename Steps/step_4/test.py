import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def test_chart_creation():
    data_path = "../../dataset.csv" 
    try:
        df = pd.read_csv(data_path)  
    except FileNotFoundError:
        print(f"File not found at {data_path}. Please check the path.")
        return

    platforms = ["PS4", "XOne", "PC", "WiiU"]
    filtered_df = df[df['platform'].isin(platforms)]
    
    try:
        sns.set(style="darkgrid")
        plt.figure(figsize=(12, 6))
        chart = sns.countplot(
            data=filtered_df, x="platform", hue="genre", order=platforms
        )
        plt.close()  
        print("Test passed: Chart created successfully.")
    except Exception as e:
        print(f"Test failed: {e}")

test_chart_creation()
