platforms = ["PS4", "XOne", "PC", "WiiU"]
filtered_df = df[df['platform'].isin(platforms)]
print(filtered_df.head())
